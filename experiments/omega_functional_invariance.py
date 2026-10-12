#!/usr/bin/env python3
"""Ω functional invariance under element/edge turnover; stdlib-only."""
import random,csv,json,statistics,hashlib,argparse
from pathlib import Path
N=60; M=150; TRIALS=50
MODES=('no_repair','random_rewire','function_aware')
def components(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    labels=[-1]*n;sizes=[];cid=0
    for s in range(n):
        if labels[s]>=0:continue
        st=[s];labels[s]=cid;sz=0
        while st:
            u=st.pop();sz+=1
            for v in adj[u]:
                if labels[v]<0:labels[v]=cid;st.append(v)
        sizes.append(sz);cid+=1
    return labels,sizes,adj
def graph(kind,seed):
    r=random.Random(seed);e=set()
    while len(e)<M:
        if kind=='modular' and r.random()<.8:
            c=r.randrange(6);a,b=r.sample(range(c*10,(c+1)*10),2)
        else:a,b=r.sample(range(N),2)
        e.add(tuple(sorted((a,b))))
    return e
def tasks(seed):
    r=random.Random(seed+91);pairs=[]
    for i in range(12):
        if i<6:
            c=i;a=r.randrange(c*10,(c+1)*10);b=r.randrange(c*10,(c+1)*10)
        else:a=r.randrange(N);b=r.randrange(N)
        while a==b:b=r.randrange(N)
        pairs.append((a,b))
    return pairs
def task_score(edges,task_pairs):
    _,_,adj=components(N,edges);ok=0
    for s,t in task_pairs:
        seen={s};st=[s]
        while st:
            u=st.pop()
            for v in adj[u]:
                if v not in seen:seen.add(v);st.append(v)
        ok+=t in seen
    return ok/len(task_pairs)
def pick(edges,mode,seed,functions):
    labels,sizes,adj=components(N,edges)
    candidates=[(a,b) for a in range(N) for b in range(a+1,N) if (a,b) not in edges and labels[a]!=labels[b]]
    if not candidates:return None
    if mode=='random_rewire':return random.Random(seed+31337).choice(candidates)
    def score(e):
        a,b=e;gain=0
        for s,t in functions:
            if labels[s]==labels[t]:continue
            if (labels[s]==labels[a] and labels[t]==labels[b]) or (labels[s]==labels[b] and labels[t]==labels[a]):gain+=1
        return (gain,sizes[labels[a]]*sizes[labels[b]],len(adj[a])+len(adj[b]))
    top=max(score(e) for e in candidates)
    return min(e for e in candidates if score(e)==top)
def main():
    p=argparse.ArgumentParser();p.add_argument('--out',default='/tmp/omega-function-invariance');args=p.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for kind in ('er','modular'):
      for damage in (.25,.45,.60):
       for turnover in (.10,.25,.40):
        for trial in range(TRIALS):
         seed=20261012+trial+int(damage*1000)*1000+int(turnover*1000)*10+(0 if kind=='er' else 9000000)
         initial=graph(kind,seed);r=random.Random(seed+123);damaged=set(initial)
         for e in r.sample(sorted(initial),round(M*damage)):damaged.remove(e)
         funcs=tasks(seed);base_score=task_score(initial,funcs);damaged_score=task_score(damaged,funcs)
         for mode in MODES:
          e=set(damaged);added=0;removed=0
          if mode!='no_repair':
           for k in range(round(len(damaged)*turnover)):
            if not e:break
            old=sorted(e)[random.Random(seed+500000+k).randrange(len(e))]
            e.remove(old);removed+=1;new=pick(e,mode,seed+k,funcs)
            if new is None:e.add(old);removed-=1;continue
            e.add(new);added+=1
          post_score=task_score(e,funcs)
          rr=random.Random(seed+808080);k_nodes=round(N*turnover);turn_edges=set(e);replaced=set(rr.sample(range(N),k_nodes))
          for v in replaced:
              inc=[x for x in turn_edges if v in x];deg=len(inc)
              for x in inc:turn_edges.remove(x)
              candidates=[u for u in range(N) if u!=v];rr.shuffle(candidates)
              for u in candidates:
                  edge=tuple(sorted((v,u)))
                  if edge not in turn_edges:
                      turn_edges.add(edge);deg-=1
                      if deg<=0:break
          after_turn_score=task_score(turn_edges,funcs);_,sizes,_=components(N,turn_edges)
          rows.append(dict(graph=kind,damage_fraction=damage,edge_turnover_fraction=turnover,trial=trial,seed=seed,mode=mode,initial_function_score=base_score,after_damage_function_score=damaged_score,after_edge_turnover_function_score=post_score,after_node_replacement_function_score=after_turn_score,function_retention_vs_initial=after_turn_score/base_score if base_score else 0,edge_count_before=len(damaged),edge_count_after=len(turn_edges),edges_replaced=added,nodes_replaced=k_nodes,lcc_after=max(sizes)/N))
    raw=out/'OMEGA-FUNCTIONAL-INVARIANCE-2026-10-12.csv'
    with raw.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    metrics=['initial_function_score','after_damage_function_score','after_edge_turnover_function_score','after_node_replacement_function_score','function_retention_vs_initial','lcc_after','edges_replaced'];groups={}
    for row in rows:
      key=(row['graph'],row['damage_fraction'],row['edge_turnover_fraction'],row['mode']);g=groups.setdefault(key,{m:[] for m in metrics})
      for m in metrics:g[m].append(float(row[m]))
    summary=[]
    for key,v in sorted(groups.items()):
      item=dict(zip(('graph','damage_fraction','edge_turnover_fraction','mode'),key));item['trials']=TRIALS
      for m,vals in v.items():item[m+'_mean']=statistics.mean(vals);item[m+'_sd']=statistics.pstdev(vals)
      summary.append(item)
    js=out/'OMEGA-FUNCTIONAL-INVARIANCE-2026-10-12-summary.json'
    js.write_text(json.dumps({'experiment':'Functional invariance under edge turnover and node replacement','nodes':N,'initial_edges':M,'trials_per_configuration':TRIALS,'graph_families':['er','modular'],'damage_fractions':[.25,.45,.60],'edge_turnover_fractions':[.10,.25,.40],'functional_tasks_per_trial':12,'rows':len(rows),'summary':summary},indent=2)+'\n')
    print('ROWS',len(rows));print('CSV_SHA256',hashlib.sha256(raw.read_bytes()).hexdigest());print('SUMMARY_SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
    for kind in ('er','modular'):
     for d in (.25,.45,.60):
      for t in (.10,.25,.40):
       sub={x['mode']:x for x in summary if x['graph']==kind and x['damage_fraction']==d and x['edge_turnover_fraction']==t}
       print(kind,'damage',d,'turnover',t,'retention no/random/aware',*[round(sub[m]['function_retention_vs_initial_mean'],3) for m in MODES])
if __name__=='__main__':main()
