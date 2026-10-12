#!/usr/bin/env python3
"""Ω delayed-feedback benchmark: four architectures, noisy observations, hidden rule shifts."""
import argparse,csv,json,random,statistics
from pathlib import Path

MOD=4
MODES=("fast_only","exploratory_only","hybrid_fixed","hybrid_confidence")
TRIALS=300
TRAIN_MIN,TRAIN_MAX=8,14
TEST_STEPS=120
SHIFT_AT=60
NOISE=0.10
FEEDBACK_DELAY=5
def step(s,x,rule):
 a,b,c=rule
 return (a*s+b*x+c)%MOD
def ruleset():
 return [(a,b,c) for a in range(MOD) for b in range(MOD) for c in range(MOD)]
def noisy_observation(rng,y):
 return (y+rng.randrange(1,MOD))%MOD if rng.random()<NOISE else y
def main():
 p=argparse.ArgumentParser();p.add_argument("--out",default="results");p.add_argument("--trials",type=int,default=TRIALS);args=p.parse_args()
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True);all_rules=ruleset();rows=[]
 for trial in range(args.trials):
  rng=random.Random(20261014+trial)
  ra=rng.choice(all_rules);rb=rng.choice(all_rules)
  while rb==ra:rb=rng.choice(all_rules)
  train=[];s=rng.randrange(MOD)
  for _ in range(rng.randint(TRAIN_MIN,TRAIN_MAX)):
   x=rng.randrange(MOD);y=step(s,x,ra);train.append((s,x,noisy_observation(rng,y)));s=y
  candidates=[q for q in all_rules if all(step(s,x,q)==y for s,x,y in train)]
  def model_table(cands):
   table={}
   for ss in range(MOD):
    for xx in range(MOD):
     votes=[0]*MOD
     for q in cands:votes[step(ss,xx,q)]+=1
     table[(ss,xx)]=max(range(MOD),key=lambda y:(votes[y],-y))
   return table
  model=model_table(candidates) if candidates else {(ss,xx):0 for ss in range(MOD) for xx in range(MOD)}
  # Pre-generate test stream; environment truth is hidden from agents.
  tests=[];state=rng.randrange(MOD)
  for i in range(TEST_STEPS):
   x=rng.randrange(MOD);rule=ra if i<SHIFT_AT else rb;y=step(state,x,rule)
   tests.append((i,state,x,y));state=y
  for mode in MODES:
   # cache is learned only from noisy initial observations
   counts={}
   for ss,xx,yy in train:counts.setdefault((ss,xx),[0]*MOD)[yy]+=1
   cache={k:max(range(MOD),key=lambda y:(v[y],-y)) for k,v in counts.items()}
   pending=[];correct=pre=post=fast=explore=abstain=feedback_used=0
   for i,ss,xx,y in tests:
    # Apply feedback that has matured; it is noisy and delayed, not immediate truth.
    ready=[item for item in pending if item[0]<=i]
    pending=[item for item in pending if item[0]>i]
    for due,ps,px,observed in ready:
     feedback_used+=1
     if mode in ("hybrid_fixed","hybrid_confidence"):
      cache[(ps,px)]=observed
    key=(ss,xx);cached=cache.get(key)
    if mode=="fast_only":
     pred=cached
     if pred is None:abstain+=1
     else:fast+=1
    elif mode=="exploratory_only":
     pred=model[key];explore+=1
    elif mode=="hybrid_fixed":
     if cached is not None:pred=cached;fast+=1
     else:pred=model[key];explore+=1
    else:
     # Confidence is estimated from cache support; low support or repeated disagreement routes to model.
     support=counts.get(key,[0]*MOD)
     conf=max(support)/sum(support) if sum(support) else 0.0
     if cached is not None and conf>=0.75:
      pred=cached;fast+=1
     else:pred=model[key];explore+=1
    if pred==y:
     correct+=1
     if i<SHIFT_AT:pre+=1
     else:post+=1
    # No direct label leaks into decision/cache; reveal a noisy label only after fixed delay.
    pending.append((i+FEEDBACK_DELAY,ss,xx,noisy_observation(rng,y)))
    # Update support only from training or mature feedback.
    if mode=="hybrid_confidence":
     for due,ps,px,obs in ready:
      if (ps,px)==key:
       counts.setdefault(key,[0]*MOD)[obs]+=1
   rows.append(dict(trial=trial,seed=20261014+trial,mode=mode,accuracy=correct/TEST_STEPS,
    pre_shift_accuracy=pre/SHIFT_AT,post_shift_accuracy=post/(TEST_STEPS-SHIFT_AT),
    fast_uses=fast,exploration_calls=explore,abstentions=abstain,feedback_labels_used=feedback_used,
    training_observations=len(train),consistent_hypotheses=len(candidates)))
 cp=out/"OMEGA-DELAYED-FEEDBACK-2026-10-12.csv"
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
   "mean_fast_uses":statistics.mean(r["fast_uses"] for r in rr),
   "mean_exploration_calls":statistics.mean(r["exploration_calls"] for r in rr),
   "mean_abstentions":statistics.mean(r["abstentions"] for r in rr)})
 result={"experiment":"Ω delayed-feedback benchmark","environment":"four-state affine rule next=(a*state+b*input+c) mod 4",
  "trials":args.trials,"rows":len(rows),"training_observations":f"{TRAIN_MIN}–{TRAIN_MAX}, {int(NOISE*100)}% corruption",
  "test_steps":TEST_STEPS,"rule_shift_after":SHIFT_AT,"feedback_delay":FEEDBACK_DELAY,
  "modes":list(MODES),"limitations":["Synthetic finite rule family.","Feedback labels are noisy and delayed but still supplied by environment.","Confidence policy is heuristic and fixed before evaluation.","No claims about general intelligence or consciousness."],"summary":summary}
 (out/"OMEGA-DELAYED-FEEDBACK-2026-10-12-summary.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(result,indent=2))
if __name__=="__main__":main()
