#!/usr/bin/env python3
"""Ω dual-contour stress benchmark: noise, regime shifts, and shared-memory ablation."""
import argparse, csv, json, random, statistics
from pathlib import Path

MOD=4
MODES=("fast_only","exploratory_only","hybrid_shared_memory","hybrid_no_shared_memory")
NOISE=0.15
TRAIN_MIN,TRAIN_MAX=6,10
TEST_STEPS=100
SHIFT_AT=50

def step(state, inp, rule):
    a,b,c=rule
    return (a*state+b*inp+c)%MOD

def all_rules():
    return [(a,b,c) for a in range(MOD) for b in range(MOD) for c in range(MOD)]

def episode(rng, rule, n, noisy=False):
    state=rng.randrange(MOD); out=[]
    for _ in range(n):
        inp=rng.randrange(MOD); actual=step(state,inp,rule)
        observed=actual
        if noisy and rng.random()<NOISE:
            observed=(actual+rng.randrange(1,MOD))%MOD
        out.append((state,inp,observed,actual))
        state=actual
    return out

def fit_candidates(observations):
    rules=all_rules()
    return [r for r in rules if all(step(s,x,r)==y for s,x,y in observations)]

def model_from_candidates(candidates):
    # Majority vote over consistent hypotheses; deterministic low-value tie-break.
    table={}
    for s in range(MOD):
        for x in range(MOD):
            votes=[0]*MOD
            for rule in candidates: votes[step(s,x,rule)]+=1
            table[(s,x)]=max(range(MOD),key=lambda y:(votes[y],-y))
    return table

def run_trial(seed):
    rng=random.Random(seed)
    rule_a=tuple(rng.randrange(MOD) for _ in range(3))
    rule_b=tuple(rng.randrange(MOD) for _ in range(3))
    while rule_b==rule_a: rule_b=tuple(rng.randrange(MOD) for _ in range(3))
    train=episode(rng,rule_a,rng.randint(TRAIN_MIN,TRAIN_MAX),noisy=True)
    candidates=fit_candidates([(s,x,y) for s,x,y,_ in train])
    model=model_from_candidates(candidates) if candidates else {(s,x):0 for s in range(MOD) for x in range(MOD)}
    # Generate test inputs/states sequentially; the state trajectory follows the true system.
    tests=[]; state=rng.randrange(MOD)
    for i in range(TEST_STEPS):
        inp=rng.randrange(MOD); active=rule_a if i<SHIFT_AT else rule_b
        actual=step(state,inp,active)
        tests.append((i,state,inp,actual,active))
        state=actual
    results=[]
    for mode in MODES:
        cache={(s,x):y for s,x,y,_ in train if sum(1 for ss,xx,yy,_ in train if ss==s and xx==x and yy==y)>
                    sum(1 for ss,xx,yy,_ in train if ss==s and xx==x and yy!=y)}
        correct=0; cache_hits=0; explore_calls=0; abstentions=0; pre_correct=0; post_correct=0
        for i,s,x,y,active in tests:
            cached=cache.get((s,x))
            if mode=="fast_only":
                pred=cached
                if pred is None: abstentions+=1
                else: cache_hits+=1
            elif mode=="exploratory_only":
                pred=model[(s,x)]; explore_calls+=1
            else:
                if cached is not None:
                    pred=cached; cache_hits+=1
                else:
                    pred=model[(s,x)]; explore_calls+=1
            ok=pred==y
            if ok: correct+=1
            if i<SHIFT_AT:
                if ok: pre_correct+=1
            else:
                if ok: post_correct+=1
            # Feedback is available after each prediction in this benchmark.
            # Shared-memory hybrid stores the actual observed transition, even if prediction was wrong.
            if mode=="hybrid_shared_memory":
                cache[(s,x)]=y
        results.append(dict(seed=seed,mode=mode,accuracy=correct/TEST_STEPS,
          pre_shift_accuracy=pre_correct/SHIFT_AT,post_shift_accuracy=post_correct/(TEST_STEPS-SHIFT_AT),
          cache_hits=cache_hits,exploration_calls=explore_calls,abstentions=abstentions,
          training_observations=len(train),consistent_hypotheses=len(candidates)))
    return results

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",default="results");ap.add_argument("--trials",type=int,default=300);args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for i in range(args.trials): rows.extend(run_trial(20261013+i))
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
    result={"experiment":"Ω dual-contour stress benchmark",
      "environment":"4-state affine transition: next=(a*state+b*input+c) mod 4",
      "hypothesis_class_size":64,"trials":args.trials,"rows":len(rows),
      "training_observations":"6–10 noisy transitions; 15% label corruption",
      "test_steps":TEST_STEPS,"regime_shift_after_step":SHIFT_AT,
      "feedback":"After each prediction, the true next state is revealed; shared-memory hybrid stores the observed transition.",
      "modes":list(MODES),
      "limitations":["The transition family is small and synthetic.","Feedback after every prediction is a strong supervision assumption.","Fast-only abstentions count as incorrect in accuracy.","No claims about consciousness or general intelligence."],
      "summary":summary}
    (out/"OMEGA-DUAL-CONTOUR-STRESS-2026-10-12-summary.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
