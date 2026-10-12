#!/usr/bin/env python3
"""Ω held-out task test with edge damage, node deletion, and role transfer."""
import random,csv,json,statistics,hashlib,argparse
from pathlib import Path
N,M,TRIALS=60,150,12
MODES=('no_repair','random_role_transfer','task_aware_role_transfer')
def comps(edges):
 a=[set() for _ in range(N)]
 for u,v in edges:a[u].add(v);a[v].add(u)
 lab=[-1]*N;sizes=[];cid=0
 for s in range(N):
  if lab[s]>=0:continue
  st=[s];lab[s]=cid;z=0
  while st:
   u=st.pop();z+=1
   for v in a[u]:
    if lab[v]<0:lab[v]=cid;st.append(v)
  sizes.append(z);cid+=1
 return lab,sizes,a
def graph(kind,seed):
 r=random.Random(seed);e=set()
 while len(e)<M:
  if kind=='modular' and r.random()<.8:
   c=r.randrange(6);u,v=r.sample(range(c*10,(c+1)*10),2)
  else:u,v=r.sample(range(N),2)
  e.add(tuple(sorted((u,v))))
 return e
def pairs(seed,offset):
 r=random.Random(seed+offset);out=[]
 while len(out)<12:
  p=tuple(r.sample(range(N),2))
  if p not in out and p[::-1] not in out:out.append(p)
 return out
def reach(edges,ps):
 _,_,a=comps(edges);hit=0
 for s,t in ps:
  seen={s};st=[s]
  while st:
   u=st.pop()
   for v in a[u]:
    if v not in seen:seen.add(v);st.append(v)
  hit+=t in seen
 return hit/len(ps)
def transfer(edges,removed,mode,train,seed,original):
 out=set(edges);used=set();r=random.Random(seed)
 for old in sorted(removed):
  ns=sorted({v if u==old else u for u,v in original if (u==old or v==old) and (v if u==old else u) not in removed})
  hosts=[h for h in range(N) if h not in removed and h not in used]
  if not hosts or not ns:continue
  if mode=='random_role_transfer':h=r.choice(hosts)
  else:
   lab,_,_=comps(out)
   def score(h):
    linked={lab[v] for v in ns};gain=0
    for s,t in train:
     if lab[s]!=lab[t] and ((lab[s]==lab[h] and lab[t] in linked) or (lab[t]==lab[h] and lab[s] in linked)):gain+=1
    return gain
   best=max(score(h) for h in hosts);h=min(x for x in hosts if score(x)==best)
  used.add(h)
  for v in ns:
   if h!=v:out.add(tuple(sorted((h,v))))
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='results');args=ap.parse_args();d=Path(args.out);d.mkdir(parents=True,exist_ok=True);rows=[]
 for kind in ('er','modular'):
  for damage in (.25,.45,.60):
   for nf in (.05,.10,.20):
    for trial in range(TRIALS):
     seed=20261012+trial+int(damage*1000)*1000+int(nf*1000)*100+(0 if kind=='er' else 7000000)
     intact=graph(kind,seed);r=random.Random(seed+121);damaged=set(intact)
     for e in r.sample(sorted(intact),round(M*damage)):damaged.remove(e)
     k=max(1,round(N*nf));removed=set(r.sample(range(N),k));damaged={e for e in damaged if e[0] not in removed and e[1] not in removed}
     train=pairs(seed,201);held=pairs(seed,902);baseheld=reach(intact,held)
     for mode in MODES:
      fixed=set(damaged) if mode=='no_repair' else transfer(damaged,removed,mode,train,seed+44,intact)
      rows.append(dict(graph=kind,edge_damage=damage,node_removal_fraction=nf,trial=trial,seed=seed,mode=mode,removed_nodes=k,train_after_damage=reach(damaged,train),heldout_after_damage=reach(damaged,held),train_after_transfer=reach(fixed,train),heldout_after_transfer=reach(fixed,held),heldout_retention_vs_intact=reach(fixed,held)/baseheld if baseheld else 0,edges_after=len(fixed),lcc_after=max(comps(fixed)[1])/N))
 raw=d/'OMEGA-HELDOUT-ROLE-TRANSFER-2026-10-12.csv'
 with raw.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 metrics=['train_after_damage','heldout_after_damage','train_after_transfer','heldout_after_transfer','heldout_retention_vs_intact','lcc_after','edges_after'];g={}
 for row in rows:
  key=(row['graph'],row['edge_damage'],row['node_removal_fraction'],row['mode']);v=g.setdefault(key,{m:[] for m in metrics})
  for m in metrics:v[m].append(float(row[m]))
 summ=[]
 for key,v in sorted(g.items()):
  z=dict(zip(('graph','edge_damage','node_removal_fraction','mode'),key));z['trials']=TRIALS
  for m,x in v.items():z[m+'_mean']=statistics.mean(x);z[m+'_sd']=statistics.pstdev(x)
  summ.append(z)
 js=d/'OMEGA-HELDOUT-ROLE-TRANSFER-2026-10-12-summary.json'
 js.write_text(json.dumps({'experiment':'Held-out functional generalization under edge damage and node removal','nodes':N,'initial_edges':M,'trials_per_configuration':TRIALS,'graph_families':['er','modular'],'edge_damage':[.25,.45,.60],'node_removal_fraction':[.05,.10,.20],'training_tasks':12,'heldout_tasks':12,'rows':len(rows),'summary':summ},indent=2)+'\n')
 print('ROWS',len(rows),'CSV_SHA256',hashlib.sha256(raw.read_bytes()).hexdigest(),'SUMMARY_SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
 for kind in ('er','modular'):
  for dm in (.25,.45,.60):
   for nf in (.05,.10,.20):
    z={x['mode']:x for x in summ if x['graph']==kind and x['edge_damage']==dm and x['node_removal_fraction']==nf}
    print(kind,dm,nf,*[round(z[m]['heldout_after_transfer_mean'],3) for m in MODES])
if __name__=='__main__':main()
