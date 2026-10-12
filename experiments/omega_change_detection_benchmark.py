#!/usr/bin/env python3
"""Ω change-detection benchmark: compare fixed routing, calibrated confidence, and no shared memory."""
import argparse,csv,json,random,statistics
from pathlib import Path
MOD=4
MODES=("fixed_shared","calibrated_shared","no_shared_memory")
TRIALS=500
STEPS=160
SHIFT=80
DELAY=5
NOISE=0.10
def step(s,x,r): return (r[0]*s+r[1]*x+r[2])%MOD
def rules():
 return [(a,b,c) for a in range(MOD) for b in range(MOD) for c in range(MOD)]
def noisy(rng,y): return (y+rng.randrange(1,MOD))%MOD if rng.random()<NOISE else y
def main():
 p=argparse.ArgumentParser();p.add_argument("--out",default="results");p.add_argument("--trials",type=int,default=TRIALS);args=p.parse_args()
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True);all_rules=rules();rows=[]
 for trial in range(args.trials):
  rng=random.Random(20261015+trial);r0=rng.choice(all_rules);r1=rng.choice(all_rules)
  while r1==r0:r1=rng.choice(all_rules)
  # Shared initial training episode, same observations for all modes.
  state=rng.randrange(MOD);train=[]
  for _ in range(rng.randint(10,16)):
   x=rng.randrange(MOD);y=step(state,x,r0);train.append((state,x,noisy(rng,y)));state=y
  candidates=[r for r in all_rules if all(step(s,x,r)==y for s,x,y in train)]
  model={}
  for s in range(MOD):
   for x in range(MOD):
    votes=[0]*MOD
    for r in candidates:votes[step(s,x,r)]+=1
    model[(s,x)]=max(range(MOD),key=lambda y:(votes[y],-y))
  # Shared hidden test trajectory, generated before model actions.
  state=rng.randrange(MOD);test=[]
  for i in range(STEPS):
   x=rng.randrange(MOD);actual=step(state,x,r0 if i<SHIFT else r1);test.append((i,state,x,actual));state=actual
  for mode in MODES:
   # Each mode gets same training data, but own memory.
   counts={}
   for s,x,y in train:counts.setdefault((s,x),[0]*MOD)[y]+=1
   cache={k:max(range(MOD),key=lambda y:(v[y],-y)) for k,v in counts.items()}
   support={k:sum(v) for k,v in counts.items()}
   pending=[];pred_errors=[];recent_errors=[];correct=pre=post=fast=explore=abstain=shift_detected=None
   correct=pre=post=fast=explore=abstain=0;detected_at=None;feedback_count=0
   for i,s,x,y in test:
    # Mature feedback enters memory only after the fixed delay.
    ready=[p for p in pending if p[0]<=i];pending=[p for p in pending if p[0]>i]
    for due,ps,px,obs,pred_at,oldpred in ready:
     feedback_count+=1
     err=int(obs!=oldpred)
     recent_errors.append((pred_at,err))
     if mode!="no_shared_memory":
      cache[(ps,px)]=obs
      support[(ps,px)]=support.get((ps,px),0)+1
    # Detect sustained mismatch in the last 8 available labels; use only matured feedback.
    recent=[e for t,e in recent_errors if t>=i-20]
    if mode=="calibrated_shared" and detected_at is None and len(recent)>=4 and sum(recent)/len(recent)>=0.5:
     detected_at=i
     cache.clear();support.clear()
    k=(s,x);cached=cache.get(k)
    if mode=="fixed_shared":
     if cached is None:pred=model[k];explore+=1
     else:pred=cached;fast+=1
    elif mode=="no_shared_memory":
     if cached is None:pred=model[k];explore+=1
     else:pred=cached;fast+=1
    else:
     # Calibrated mode uses cached rules only with support and stable recent errors.
     err_rate=(sum(recent)/len(recent)) if recent else 0.0
     conf=support.get(k,0)/(support.get(k,0)+2)
     if cached is not None and conf>=0.6 and err_rate<0.35:pred=cached;fast+=1
     else:pred=model[k];explore+=1
    ok=int(pred==y);correct+=ok
    if i<SHIFT:pre+=ok
    else:post+=ok
    pending.append((i+DELAY,s,x,noisy(rng,y),i,pred))
   rows.append(dict(trial=trial,seed=20261015+trial,mode=mode,accuracy=correct/STEPS,
    pre_shift_accuracy=pre/SHIFT,post_shift_accuracy=post/(STEPS-SHIFT),fast_uses=fast,
    exploration_calls=explore,abstentions=abstain,feedback_labels_used=feedback_count,
    change_detected_at=detected_at if detected_at is not None else -1,
    training_observations=len(train),consistent_hypotheses=len(candidates)))
 cp=out/"OMEGA-CHANGE-DETECTION-2026-10-12.csv"
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
   "mean_detection_delay":statistics.mean(r["change_detected_at"]-SHIFT for r in rr if r["change_detected_at"]>=0) if any(r["change_detected_at"]>=0 for r in rr) else None,
   "detection_rate":sum(r["change_detected_at"]>=0 for r in rr)/len(rr)})
 result={"experiment":"Ω change detection and memory ablation","trials":args.trials,"rows":len(rows),
  "rule":"next=(a*state+b*input+c) mod 4","training":"10–16 observations, 10% noisy labels",
  "test_steps":STEPS,"rule_shift_after":SHIFT,"feedback_delay":DELAY,"feedback_noise":NOISE,
  "modes":list(MODES),"limitations":["Finite synthetic rules only.","Change detection relies on delayed noisy labels.","Model hypothesis set is fixed from initial training; it cannot infer a wholly new rule unless cache feedback covers a queried transition.","No claims about general intelligence or consciousness."],"summary":summary}
 (out/"OMEGA-CHANGE-DETECTION-2026-10-12-summary.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(result,indent=2))
if __name__=="__main__":main()
