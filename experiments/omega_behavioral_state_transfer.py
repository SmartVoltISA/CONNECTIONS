#!/usr/bin/env python3
"""Minimal reproducible Ω behavioral-state transfer benchmark (Python stdlib)."""
import random,csv,json,statistics,hashlib,argparse
from pathlib import Path
N,M,TRIALS=48,112,60
MODES=('no_transfer','random_successor','state_aware_successor')
def graph(kind,seed):
 r=random.Random(seed);e=set()
 while len(e)<M:
  if kind=='modular' and r.random()<.8:
   c=r.randrange(6);u,v=r.sample(range(c*8,(c+1)*8),2)
  else:u,v=r.sample(range(N),2)
  e.add(tuple(sorted((u,v))))
 return e
def pairs(seed,off,n=16):
 r=random.Random(seed+off);out=[]
 while len(out)<n:
  p=tuple(r.sample(range(N),2))
  if p not in out and p[::-1] not in out:out.append(p)
 return out
def route(edges,ps):
 a=[set() for _ in range(N)]
 for u,v in edges:a[u].add(v);a[v].add(u)
 score=0
 for s,t in ps:
  seen={s};st=[s]
  while st:
   u=st.pop()
   for v in a[u]:
    if v not in seen:seen.add(v);st.append(v)
  score+=t in seen
 return score/len(ps)
def main():
 p=argparse.ArgumentParser();p.add_argument('--out',default='results');args=p.parse_args();d=Path(args.out);d.mkdir(parents=True,exist_ok=True);rows=[]
 for kind in ('er','modular'):
  for el in (.25,.50,.65):
   for nl in (.05,.15,.25):
    for trial in range(TRIALS):
     seed=20261012+trial+int(el*1000)*1000+int(nl*100)*10+(0 if kind=='er' else 900000)
     intact=graph(kind,seed);rr=random.Random(seed+91);damaged=set(intact)
     for edge in rr.sample(sorted(intact),round(M*el)):damaged.remove(edge)
     k=max(1,round(N*nl));removed=set(rr.sample(range(N),k));surv=[x for x in range(N) if x not in removed]
     damaged={e for e in damaged if not (e[0] in removed or e[1] in removed)}
     sr=random.Random(seed+401);state=[sr.randrange(4) for _ in range(N)]
     adj=[set() for _ in range(N)]
     for u,v in intact:adj[u].add(v);adj[v].add(u)
     train=pairs(seed,201);held=pairs(seed,902);test_inputs=(2,3)
     for mode in MODES:
      fixed=set(damaged);new=list(state);successor={};used=set()
      if mode!='no_transfer':
       rng=random.Random(seed+701)
       for old in sorted(removed):
        hosts=[h for h in surv if h not in used]
        if not hosts:continue
        neigh=[v for v in adj[old] if v in surv]
        if mode=='random_successor':h=rng.choice(hosts)
        else:
         vals=[state[v] for v in neigh] or [state[v] for v in surv]
         counts=[vals.count(q) for q in range(4)];inferred=max(range(4),key=lambda q:(counts[q],-q))
         degree={h:sum(h in edge for edge in damaged) for h in hosts}
         h=max(hosts,key=lambda z:(state[z]==inferred,degree[z],-z))
         new[h]=inferred
        successor[old]=h;used.add(h)
        for v in neigh:
         if h!=v:fixed.add(tuple(sorted((h,v))))
      beh=[sum((new[h]^x)==(state[old]^x) for x in test_inputs)/len(test_inputs) for old,h in successor.items()]
      rows.append(dict(graph=kind,edge_loss=el,node_loss=nl,trial=trial,seed=seed,mode=mode,removed_nodes=k,heldout_behavior_match=statistics.mean(beh) if beh else 0,heldout_route_reachability=route(fixed,held),routes_after_damage=route(damaged,held),routes_after_transfer=route(fixed,held),successors_assigned=len(successor)))
 raw=d/'OMEGA-BEHAVIORAL-STATE-TRANSFER-2026-10-12.csv'
 with raw.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 metrics=['heldout_behavior_match','heldout_route_reachability','routes_after_damage','routes_after_transfer','successors_assigned'];groups={}
 for row in rows:
  key=(row['graph'],row['edge_loss'],row['node_loss'],row['mode']);g=groups.setdefault(key,{m:[] for m in metrics})
  for m in metrics:g[m].append(float(row[m]))
 summary=[]
 for key,v in sorted(groups.items()):
  z=dict(zip(('graph','edge_loss','node_loss','mode'),key));z['trials']=TRIALS
  for m,x in v.items():z[m+'_mean']=statistics.mean(x);z[m+'_sd']=statistics.pstdev(x)
  summary.append(z)
 js=d/'OMEGA-BEHAVIORAL-STATE-TRANSFER-2026-10-12-summary.json'
 js.write_text(json.dumps({'experiment':'Behavioral state transfer under node removal','nodes':N,'initial_edges':M,'trials_per_configuration':TRIALS,'graph_families':['er','modular'],'edge_loss':[.25,.50,.65],'node_loss':[.05,.15,.25],'state_alphabet_size':4,'heldout_inputs':[2,3],'rows':len(rows),'summary':summary},indent=2)+'\n')
 print('rows',len(rows),'csv_sha256',hashlib.sha256(raw.read_bytes()).hexdigest(),'summary_sha256',hashlib.sha256(js.read_bytes()).hexdigest())
if __name__=='__main__':main()
