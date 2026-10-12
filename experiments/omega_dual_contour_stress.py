#!/usr/bin/env python3
"""Ω dual-contour stress benchmark: noisy observations, rule shift, shared-memory ablation."""
import argparse,csv,json,random,statistics
from pathlib import Path
MOD=4
MODES=("fast_only","exploratory_only","hybrid_shared_memory","hybrid_no_shared_memory")
NOISE=0.15
TEST_STEPS=100
SHIFT_AT=50
def step(s,x,rule):
 a,b,c=rule
 return (a*s+b*x+c)%MOD
def all_rules():
 return [(a,b,c) for a in range(MOD) for b in range(MOD) for c in range(MOD)]
def episode(rng,rule,n,noisy=False):
 s=rng.randrange(MOD);out=[]
 for _ in range(n):
  x=rng.randrange(MOD);actual=step(s,x,rule);observed=actual
  if noisy and rng.random()<NOISE: observed=(actual+rng.randrange(1,MOD))%MOD
  out.append((s,x,observed,actual));s=actual
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument("--out",default="results");p.add_argument("--trials",type=int,default=300);args=p.parse_args()
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True);rules=all_rules();rows=[]
 for trial in range(args.trials):
  rng=random.Random(20261013+trial);ra=rng.choice(rules);rb=rng.choice(rules)
  while rb==ra:rb=rng.choice(rules)
  train=episode(rng,ra,rng.randint(6,10),True)
  candidates=[rule for rule in rules if all(step(s,x,rule)==y for s,x,y,_ in train)]
  model={}
  for s in range(MOD):
   for x in range(MOD):
    votes=[0]*MOD
    for rule in candidates:votes[step(s,x,rule)]+=1
    model[(s,x)]=max(range(MOD),key=lambda y:(votes[y],-y))
  state=rng.randrange(MOD);tests=[]
  for i in range(TEST_STEPS):
   x=rng.randrange(MOD);active=ra if i<SHIFT_AT else rb;y=step(state,x,active)
   tests.append((i,state,x,y));state=y
  for mode in MODES:
   counts={}
   for s,x,y,_ in train:counts.setdefault((s,x),[0]*MOD)[y]+=1
   cache={k:max(range(MOD),key=lambda y:(v[y],-y)) for k,v in counts.items()}
   correct=pre=post=hits=explore=abstain=0
   for i,s,x,y in tests:
    key=(s,x)
    if mode=="fast_only":
     pred=cache.get(key)
     if pred is None:abstain+=1
     else:hits+=1
    elif mode=="exploratory_only":pred=model[key];explore+=1
    elif key in cache:pred=cache[key];hits+=1
    else:pred=model[key];explore+=1
    if pred==y:
     correct+=1
     if i<SHIFT_AT:pre+=1
     else:post+=1
    if mode=="hybrid_shared_memory":cache[key]=y
   rows.append(dict(trial=trial,seed=20261013+trial,mode=mode,accuracy=correct/TEST_STEPS,
    pre_shift_accuracy=pre/SHIFT_AT,post_shift_accuracy=post/(TEST_STEPS-SHIFT_AT),
    cache_hits=hits,exploration_calls=explore,abstentions=abstain,
    training_observations=len(train),consistent_hypotheses=len(candidates)))
 cp=out/"OMEGA-DUAL-CONTOUR-STRESS-2026-10-12.csv"
 with cp.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summary=[]
 for mode in MODES:
  rr=[r for r in rows if r["mode"]==mode]
  summary.append({"mode":mode,"trials":args.trials,
   "mean_accuracy":statistics.mean(r["accuracy"] for r in rr),
   "sd_accuracy":statistics.pstdev(r["accuracy"] for r in rr),
   "mean_pre_shift_accuracy":statistics.mean(r["pre_shift_accuracy"] for r in rr),
   "mean_post_shift_accuracy":statistics.mean(r["post_shift_accuracy"] for r in rr),
   "mean_cache_hits":statistics.mean(r["cache_hits"] for r in rr),
   "mean_exploration_calls":statistics.mean(r["exploration_calls"] for r in rr),
   "mean_abstentions":statistics.mean(r["abstentions"] for r in rr)})
 result={"experiment":"Ω dual-contour stress benchmark","environment":"four-state affine transition: next=(a*state+b*input+c) mod 4",
  "hypothesis_class_size":64,"trials":args.trials,"rows":len(rows),"training":"6–10 transitions; 15% corrupted observations",
  "test_steps":TEST_STEPS,"regime_shift_after_step":SHIFT_AT,
  "feedback":"True next state is revealed after each prediction. Shared-memory hybrid stores this feedback.",
  "modes":list(MODES),"limitations":["Small synthetic rule family.","Strong feedback assumption.","Abstentions count as incorrect in accuracy.","No claim about consciousness or general intelligence."],"summary":summary}
 (out/"OMEGA-DUAL-CONTOUR-STRESS-2026-10-12-summary.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(result,indent=2))
if __name__=="__main__":main()
