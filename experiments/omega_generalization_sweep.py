#!/usr/bin/env python3
"""Reproducible Ω repair-strategy generalization sweep; Python standard library only."""
import argparse,csv,json,random,statistics,hashlib
from pathlib import Path
N=60; INITIAL_EDGES=150; TRIALS=30
def connected_components(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    comp=[-1]*n; sizes=[]; cid=0
    for s in range(n):
        if comp[s]>=0: continue
        stack=[s];comp[s]=cid;size=0
        while stack:
            u=stack.pop();size+=1
            for v in adj[u]:
                if comp[v]<0: comp[v]=cid;stack.append(v)
        sizes.append(size);cid+=1
    return comp,sizes,adj
def make_graph(kind, seed):
    r=random.Random(seed); edges=set()
    if kind=='er':
        while len(edges)<INITIAL_EDGES:
            a,b=r.sample(range(N),2);edges.add(tuple(sorted((a,b))))
    else:
        while len(edges)<INITIAL_EDGES:
            if r.random()<.8:
                c=r.randrange(6);a,b=r.sample(range(c*10,(c+1)*10),2)
            else:
                ca,cb=r.sample(range(6),2);a=r.randrange(ca*10,(ca+1)*10);b=r.randrange(cb*10,(cb+1)*10)
            edges.add(tuple(sorted((a,b))))
    return edges
def pairs(seed, offset, count=8):
    r=random.Random(seed+offset);out=[]
    while len(out)<count:
        a,b=r.sample(range(N),2)
        if (a,b) not in out and (b,a) not in out:out.append((a,b))
    return out
def reach_rate(edges,tasks):
    _,_,adj=connected_components(N,edges);total=0
    for a,b in tasks:
        seen={a};stack=[a]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in seen:seen.add(v);stack.append(v)
        total+=b in seen
    return total/len(tasks)
def choose_repair(edges,train,mode,seed):
    comp,sizes,adj=connected_components(N,edges)
    candidates=[(a,b) for a in range(N) for b in range(a+1,N) if (a,b) not in edges and comp[a]!=comp[b]]
    if not candidates:return None
    if mode=='random_bridge':return random.Random(seed+900001).choice(candidates)
    def score(e):
        a,b=e;new=0
        for s,t in train:
            if comp[s]==comp[t]:continue
            if (comp[s]==comp[a] and comp[t]==comp[b]) or (comp[s]==comp[b] and comp[t]==comp[a]):new+=1
        return (new,sizes[comp[a]]*sizes[comp[b]],len(adj[a])+len(adj[b]))
    best=max(score(e) for e in candidates)
    return min(e for e in candidates if score(e)==best)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='/tmp/omega-sweep');args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for kind in ['er','modular']:
      for damage in [.25,.45,.60]:
       for budget in [1,2,4]:
        for trial in range(TRIALS):
         seed=20261012+trial+int(damage*1000)*100+budget*10000+(0 if kind=='er' else 5000000)
         base=make_graph(kind,seed);r=random.Random(seed+111);damaged=set(base)
         for e in r.sample(sorted(base),round(len(base)*damage)):damaged.remove(e)
         train=pairs(seed,222);test=pairs(seed,333)
         for mode in ['no_repair','random_bridge','task_aware']:
          edges=set(damaged);added=0
          if mode!='no_repair':
           for k in range(budget):
            e=choose_repair(edges,train,mode,seed+k*17)
            if e is None:break
            edges.add(e);added+=1
          after_train=reach_rate(edges,train);after_test=reach_rate(edges,test)
          _,sizes,_=connected_components(N,edges)
          r2=random.Random(seed+777777);damaged2=set(edges);nremove=round(len(damaged2)*.10)
          for e in r2.sample(sorted(damaged2),min(nremove,len(damaged2))):damaged2.remove(e)
          second_train=reach_rate(damaged2,train);second_test=reach_rate(damaged2,test)
          _,sizes2,_=connected_components(N,damaged2)
          rows.append(dict(graph=kind,damage_fraction=damage,budget=budget,trial=trial,seed=seed,mode=mode,edges_added=added,train_reach_after=after_train,heldout_reach_after=after_test,lcc_after=max(sizes)/N,train_reach_second_damage=second_train,heldout_reach_second_damage=second_test,lcc_second_damage=max(sizes2)/N))
    csvpath=out/'OMEGA-GENERALIZATION-SWEEP-2026-10-12.csv'
    with csvpath.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    metrics=['train_reach_after','heldout_reach_after','lcc_after','train_reach_second_damage','heldout_reach_second_damage','lcc_second_damage','edges_added'];grouped={}
    for row in rows:
        key=(row['graph'],row['damage_fraction'],row['budget'],row['mode']);grouped.setdefault(key,{m:[] for m in metrics})
        for m in metrics:grouped[key][m].append(float(row[m]))
    summary=[]
    for key,vals in sorted(grouped.items()):
        item=dict(zip(['graph','damage_fraction','budget','mode'],key));item['trials']=TRIALS
        for m,x in vals.items():item[m+'_mean']=statistics.mean(x);item[m+'_sd']=statistics.pstdev(x)
        summary.append(item)
    js=out/'OMEGA-GENERALIZATION-SWEEP-2026-10-12-summary.json'
    js.write_text(json.dumps({'experiment':'Omega repair strategy generalization sweep','n':N,'initial_edges':INITIAL_EDGES,'trials_per_configuration':TRIALS,'graph_families':['er','modular'],'damage_fractions':[.25,.45,.60],'repair_budgets':[1,2,4],'train_pairs':8,'heldout_pairs':8,'secondary_damage_fraction':.10,'rows':len(rows),'summary':summary},indent=2)+'\n')
    print('ROWS',len(rows));print('CSV SHA256',hashlib.sha256(csvpath.read_bytes()).hexdigest());print('SUMMARY SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
    for graph in ['er','modular']:
      for damage in [.25,.45,.60]:
       for budget in [1,2,4]:
        subset={x['mode']:x for x in summary if x['graph']==graph and x['damage_fraction']==damage and x['budget']==budget};a=subset['task_aware'];b=subset['random_bridge']
        print(graph,damage,budget,'heldout_after_delta',round(a['heldout_reach_after_mean']-b['heldout_reach_after_mean'],4),'heldout_second_delta',round(a['heldout_reach_second_damage_mean']-b['heldout_reach_second_damage_mean'],4),'train_delta',round(a['train_reach_after_mean']-b['train_reach_after_mean'],4))
if __name__=='__main__':main()
