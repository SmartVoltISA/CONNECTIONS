#!/usr/bin/env python3
"""Ω dual-contour benchmark: fast cached rules vs exploratory model inference vs hybrid."""
import argparse, csv, hashlib, json, random, statistics
from pathlib import Path

MOD = 4
TRIALS = 300
MODES = ("fast_cache", "exploratory_model", "hybrid")
# Small, explicit hypothesis class. The environment chooses a,b,c and transitions mod 4.
def step(s, x, rule):
    a, b, c = rule
    return (a*s + b*x + c) % MOD

def all_rules():
    return [(a,b,c) for a in range(MOD) for b in range(MOD) for c in range(MOD)]

def generate_episode(r, rule, n, start=None):
    s = r.randrange(MOD) if start is None else start
    rows=[]
    for _ in range(n):
        x=r.randrange(MOD)
        y=step(s,x,rule)
        rows.append((s,x,y))
        s=y
    return rows

def fit_rules(observations):
    return [rule for rule in all_rules()
            if all(step(s,x,rule)==y for s,x,y in observations)]

def cache_predict(cache, s, x):
    counts=cache.get((s,x))
    if not counts: return None
    return max(range(MOD), key=lambda y:(counts[y],-y))

def evaluate(seed):
    r=random.Random(seed)
    truth=tuple(r.randrange(MOD) for _ in range(3))
    # Deliberately limited training; evaluation also includes unseen state/input pairs.
    train=generate_episode(r,truth, r.randint(5,9))
    test=generate_episode(r,truth,120)
    cache={}
    for s,x,y in train:
        cache.setdefault((s,x),[0]*MOD)[y]+=1
    candidates=fit_rules(train)
    # Deterministic tie-break: model uncertainty is recorded, not hidden.
    inferred=candidates[0] if candidates else None
    rows=[]
    for mode in MODES:
        correct=0; fast_hits=0; explore_calls=0; abstentions=0
        for s,x,y in test:
            cached=cache_predict(cache,s,x)
            if mode=="fast_cache":
                pred=cached
                if pred is None: abstentions+=1
                else: fast_hits+=1
            elif mode=="exploratory_model":
                explore_calls+=1
                pred=step(s,x,inferred) if inferred is not None else None
            else:
                if cached is not None:
                    pred=cached; fast_hits+=1
                else:
                    explore_calls+=1
                    pred=step(s,x,inferred) if inferred is not None else None
                    # Once a prediction is observed, hybrid writes verified transition to its shared cache.
                    # This is online adaptation; a wrong first guess is not treated as verified.
                    if pred == y:
                        cache.setdefault((s,x),[0]*MOD)[y]+=1
            if pred==y: correct+=1
        rows.append(dict(seed=seed,mode=mode,accuracy=correct/len(test),
                         fast_cache_uses=fast_hits,exploration_calls=explore_calls,
                         abstentions=abstentions,training_rows=len(train),
                         consistent_hypotheses=len(candidates),
                         rule_identified=(len(candidates)==1)))
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='results')
    ap.add_argument('--trials',type=int,default=TRIALS)
    args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for i in range(args.trials): rows.extend(evaluate(20261012+i))
    csv_path=out/'OMEGA-DUAL-CONTOUR-BENCHMARK-2026-10-12.csv'
    with csv_path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary=[]
    for mode in MODES:
        subset=[r for r in rows if r['mode']==mode]
        summary.append({
            'mode':mode,'trials':args.trials,
            'mean_accuracy':statistics.mean(x['accuracy'] for x in subset),
            'sd_accuracy':statistics.pstdev(x['accuracy'] for x in subset),
            'mean_exploration_calls':statistics.mean(x['exploration_calls'] for x in subset),
            'mean_fast_cache_uses':statistics.mean(x['fast_cache_uses'] for x in subset),
            'mean_abstentions':statistics.mean(x['abstentions'] for x in subset)
        })
    result={'experiment':'Fast vs exploratory vs hybrid dual contour',
      'environment':'4-state deterministic affine transition: next=(a*state+b*input+c) mod 4',
      'hypothesis_class_size':64,'trials':args.trials,'rows':len(rows),
      'training_length':'5–9 transitions','test_length':120,
      'caveat':'Synthetic finite hypothesis class only; not evidence of consciousness or general intelligence.',
      'summary':summary}
    js=out/'OMEGA-DUAL-CONTOUR-BENCHMARK-2026-10-12-summary.json'
    js.write_text(json.dumps(result,indent=2)+'\n')
    print('CSV_SHA256',hashlib.sha256(csv_path.read_bytes()).hexdigest())
    print('SUMMARY_SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
