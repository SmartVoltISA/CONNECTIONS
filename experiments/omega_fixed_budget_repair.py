#!/usr/bin/env python3
"""Ω-Stand fixed-budget repair experiment. Python stdlib only."""
import random, itertools, json, statistics, csv, argparse
from pathlib import Path

N=60
M=150
BUDGET=2
TRIALS=200
SEED_START=20261012

def components(adj):
    comp=[-1]*len(adj); groups=[]
    for s in range(len(adj)):
        if comp[s]>=0: continue
        cid=len(groups); comp[s]=cid; stack=[s]; group=[]
        while stack:
            u=stack.pop(); group.append(u)
            for v in adj[u]:
                if comp[v]<0: comp[v]=cid; stack.append(v)
        groups.append(group)
    return comp,groups

def reachable(adj,s,t):
    if s==t:return True
    seen={s}; stack=[s]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v==t:return True
            if v not in seen: seen.add(v); stack.append(v)
    return False

def reach_fraction(adj,pairs):
    return sum(reachable(adj,s,t) for s,t in pairs)/len(pairs)

def add_edge(adj,edges,e):
    a,b=e
    if a==b or b in adj[a]: return False
    adj[a].add(b); adj[b].add(a); edges.add(tuple(sorted(e))); return True

def run_trial(seed):
    rng=random.Random(seed)
    all_edges=list(itertools.combinations(range(N),2))
    initial=set(rng.sample(all_edges,M))
    terminals=rng.sample(range(N),16)
    pairs=list(zip(terminals[::2],terminals[1::2]))
    damaged={e for e in initial if rng.random()>=0.45}
    base=[set() for _ in range(N)]
    for a,b in damaged: base[a].add(b); base[b].add(a)
    base_reach=reach_fraction(base,pairs)
    _,base_groups=components(base)
    rows=[]
    for mode in ('no_repair','random_bridge','task_aware'):
        adj=[set(x) for x in base]; edges=set(damaged)
        rr=random.Random(seed+{'no_repair':0,'random_bridge':1,'task_aware':2}[mode]*99991)
        if mode!='no_repair':
            for _ in range(BUDGET):
                comp,groups=components(adj); candidates=[]
                for a in range(N):
                    for b in range(a+1,N):
                        if comp[a]!=comp[b] and b not in adj[a]: candidates.append((a,b))
                if not candidates: break
                if mode=='random_bridge':
                    chosen=rr.choice(candidates)
                else:
                    best=None; opts=[]
                    for a,b in candidates:
                        gain=sum(1 for s,t in pairs if not reachable(adj,s,t) and
                            ((comp[s]==comp[a] and comp[t]==comp[b]) or
                             (comp[s]==comp[b] and comp[t]==comp[a])))
                        score=(gain,len(groups[comp[a]])*len(groups[comp[b]]),len(adj[a])+len(adj[b]))
                        if best is None or score>best: best=score; opts=[(a,b)]
                        elif score==best: opts.append((a,b))
                    chosen=rr.choice(opts)
                add_edge(adj,edges,chosen)
        after_reach=reach_fraction(adj,pairs)
        _,groups_after=components(adj)
        after_lcc=max(map(len,groups_after))/N
        edges_added=len(edges)-len(damaged)
        rr2=random.Random(seed+700000)
        for e in sorted(list(edges)):
            if rr2.random()<0.10:
                a,b=e; adj[a].discard(b); adj[b].discard(a); edges.discard(e)
        second_reach=reach_fraction(adj,pairs)
        _,groups_second=components(adj)
        second_lcc=max(map(len,groups_second))/N
        rows.append(dict(seed=seed,mode=mode,base_reach=base_reach,after_reach=after_reach,
          second_reach=second_reach,base_lcc=max(map(len,base_groups))/N,after_lcc=after_lcc,
          second_lcc=max(map(len,groups_second))/N,components_after_damage=len(base_groups),
          edges_added=edges_added))
    return rows

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='omega-stand-results')
    parser.add_argument('--trials',type=int,default=TRIALS)
    args=parser.parse_args()
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for seed in range(SEED_START,SEED_START+args.trials): rows.extend(run_trial(seed))
    summary={'parameters':{'nodes':N,'initial_edges':M,'edge_damage_fraction':0.45,
      'repair_budget_edges':BUDGET,'second_damage_fraction':0.10,'trials':args.trials,
      'seed_start':SEED_START,'task_pairs_per_trial':8},
      'summary':{}}
    for mode in ('no_repair','random_bridge','task_aware'):
        subset=[r for r in rows if r['mode']==mode]; summary['summary'][mode]={}
        for key in ('base_reach','after_reach','second_reach','base_lcc','after_lcc',
                    'second_lcc','components_after_damage','edges_added'):
            vals=[r[key] for r in subset]
            summary['summary'][mode][key]={'mean':statistics.mean(vals),
              'population_sd':statistics.pstdev(vals),'min':min(vals),'max':max(vals)}
    with (out/'raw_trials.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys()); writer.writeheader(); writer.writerows(rows)
    (out/'summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
