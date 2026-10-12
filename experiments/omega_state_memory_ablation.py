#!/usr/bin/env python3
"""Ω role + state/memory continuity ablation, stdlib only."""
import random,csv,json,statistics,hashlib,argparse
from pathlib import Path
N,M,TRIALS=60,150,40
MODES=('no_transfer','role_only','state_only','role_and_state')
def graph(kind,seed):
 r=random.Random(seed);e=set()
 while len(e)<M:
  if kind=='modular' and r.random()<.8:
   c=r.randrange(6);u,v=r.sample(range(c*10,(c+1)*10),2)
  else:u,v=r.sample(range(N),2)
  e.add(tuple(sorted((u,v))))
 return e
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
def reach(edges,pairs):
 _,_,a=comps(edges);out=0
 for s,t in pairs:
  seen={s};st=[s]
  while st:
   u=st.pop()
   for v in a[u]:
    if v not in seen:seen.add(v);st.append(v)
  out+=t in seen
 return out/len(pairs)
def make_tasks(seed,offset,n=12):
 r=random.Random(seed+offset);out=[]
 while len(out)<n:
  p=tuple(r.sample(range(N),2))
  if p not in out and p[::-1] not in out:out.append(p)
 return out
def make_memory(seed):
 r=random.Random(seed+808);return [r.randrange(4) for _ in range(N)]
def transfer(edges,removed,mode,train,memory,seed,original):
 out=set(edges);hosts=[h for h in range(N) if h not in removed];r=random.Random(seed)
 # state is a 4-bit categorical state; removed-node state must be assigned to its replacement
 state=list(memory);state_map={}
 for old in sorted(removed):
  neigh=sorted({v if u==old else u for u,v in original if (u==old or v==old) and (v if u==old else u) not in removed})
  if not hosts:continue
  if mode=='role_only':h=r.choice(hosts)
  elif mode=='state_only':h=min(hosts,key=lambda x:(state[x]!=state[old],x))
  else:
   def score(h):
    lab,_,_=comps(out);linkgain=0
    for s,t in train:
     if lab[s]!=lab[t] and ((lab[s]==lab[h] and any(lab[z]==lab[t] for z in neigh)) or (lab[t]==lab[h] and any(lab[z]==lab[s] for z in neigh))):linkgain+=1
    return (linkgain,state[h]==state[old],-h)
   h=max(hosts,key=score)
  state_map[old]=h
  if mode in ('state_only','role_and_state'):state[h]=state[old]
  if mode in ('role_only','role_and_state'):
   for v in neigh:
    if h!=v:out.add(tuple(sorted((h,v))))
  hosts.remove(h)
 return out,state,state_map
def state_retention(initial,final,removed,state_map):
 # score states for surviving roles only; transferred state counts only when the transfer mode copies it.
 eligible=[i for i in range(N) if i not in removed]
 if not eligible:return 0
 return sum(final[i]==initial[i] for i in eligible)/len(eligible)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='results');args=ap.parse_args();d=Path(args.out);d.mkdir(parents=True,exist_ok=True);rows=[]
 for kind in ('er','modular'):
  for damage in (.25,.45,.60):
   for nodefrac in (.05,.10,.20):
    for trial in range(TRIALS):
     seed=20261012+trial+int(damage*1000)*1000+int(nodefrac*1000)*100+(0 if kind=='er' else 8000000)
     intact=graph(kind,seed);rr=random.Random(seed+121);damaged=set(intact)
     for e in rr.sample(sorted(intact),round(M*damage)):damaged.remove(e)
     k=max(1,round(N*nodefrac));removed=set(rr.sample(range(N),k));damaged={e for e in damaged if e[0] not in removed and e[1] not in removed}
     train=make_tasks(seed,201);held=make_tasks(seed,902);mem=make_memory(seed);base=reach(intact,held)
     for mode in MODES:
      if mode=='no_transfer':fixed=set(damaged);newmem=list(mem);mapping={}
      else:fixed,newmem,mapping=transfer(damaged,removed,mode,train,mem,seed+44,intact)
      # Evaluate held-out tasks plus independent state probes (one expected categorical state per original node).
      held_score=reach(fixed,held);survivors=[i for i in range(N) if i not in removed]
      state_score=sum(newmem[i]==mem[i] for i in survivors)/len(survivors)
      transferred_state_score=sum(newmem[mapping[i]]==mem[i] for i in mapping if mode in ('state_only','role_and_state'))/max(1,sum(i in mapping for i in removed)) if mode in ('state_only','role_and_state') else 0
      rows.append(dict(graph=kind,edge_damage=damage,node_removal_fraction=nodefrac,trial=trial,seed=seed,mode=mode,removed_nodes=k,heldout_intact=base,heldout_after_damage=reach(damaged,held),heldout_after_transfer=held_score,heldout_retention_vs_intact=held_score/base if base else 0,survivor_state_retention=state_score,removed_node_state_transfer_accuracy=transferred_state_score,edges_after=len(fixed),lcc_after=max(comps(fixed)[1])/N))
 raw=d/'OMEGA-STATE-MEMORY-ABLATION-2026-10-12.csv'
 with raw.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 metrics=['heldout_after_damage','heldout_after_transfer','heldout_retention_vs_intact','survivor_state_retention','removed_node_state_transfer_accuracy','lcc_after'];g={}
 for row in rows:
  key=(row['graph'],row['edge_damage'],row['node_removal_fraction'],row['mode']);v=g.setdefault(key,{m:[] for m in metrics})
  for m in metrics:v[m].append(float(row[m]))
 summ=[]
 for key,v in sorted(g.items()):
  z=dict(zip(('graph','edge_damage','node_removal_fraction','mode'),key));z['trials']=TRIALS
  for m,x in v.items():z[m+'_mean']=statistics.mean(x);z[m+'_sd']=statistics.pstdev(x)
  summ.append(z)
 js=d/'OMEGA-STATE-MEMORY-ABLATION-2026-10-12-summary.json'
 js.write_text(json.dumps({'experiment':'Role transfer vs state/memory transfer ablation','nodes':N,'initial_edges':M,'trials_per_configuration':TRIALS,'graph_families':['er','modular'],'edge_damage':[.25,.45,.60],'node_removal_fraction':[.05,.10,.20],'training_tasks':12,'heldout_tasks':12,'state_alphabet_size':4,'rows':len(rows),'summary':summ},indent=2)+'\n')
 print('ROWS',len(rows),'CSV_SHA256',hashlib.sha256(raw.read_bytes()).hexdigest(),'SUMMARY_SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
 for kind in ('er','modular'):
  for dm in (.25,.45,.60):
   for nf in (.05,.10,.20):
    z={x['mode']:x for x in summ if x['graph']==kind and x['edge_damage']==dm and x['node_removal_fraction']==nf}
    print(kind,dm,nf,'heldout',*[round(z[m]['heldout_after_transfer_mean'],3) for m in MODES],'state-xfer',*[round(z[m]['removed_node_state_transfer_accuracy_mean'],3) for m in MODES])
if __name__=='__main__':main()
