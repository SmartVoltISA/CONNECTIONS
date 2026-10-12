#!/usr/bin/env python3
"""Sequence-dependent state learning benchmark; Python standard library only."""
import random,csv,json,statistics,hashlib,argparse
from pathlib import Path
TRIALS=80
MODES=('stateless_baseline','transition_learning','recurrent_state_model')
def seq(r,n): return [r.randrange(2) for _ in range(n)]
def target(start,xs):
 s=start;ys=[]
 for x in xs:
  s ^= x;ys.append(s)
 return ys
def learn(examples):
 counts={(s,x):[0,0] for s in (0,1) for x in (0,1)}
 for start,xs in examples:
  s=start
  for x in xs:
   y=s^x;counts[(s,x)][y]+=1;s=y
 return {k:max((0,1),key=lambda y:(v[y],-y)) for k,v in counts.items()}
def predict(model,start,xs):
 s=start;ys=[]
 for x in xs:
  s=model[(s,x)];ys.append(s)
 return ys
def score(pred,truth):
 return sum(a==b for p,t in zip(pred,truth) for a,b in zip(p,t))/sum(len(t) for t in truth)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',default='results');a=ap.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True);rows=[]
 for trial in range(TRIALS):
  seed=20261012+trial;r=random.Random(seed)
  train=[(r.randrange(2),seq(r,r.randint(2,6))) for _ in range(40)]
  test=[(r.randrange(2),seq(r,r.randint(7,12))) for _ in range(50)]
  truth=[target(s,xs) for s,xs in test]
  stateless=[[x for x in xs] for _,xs in test]
  model=learn(train);recurrent=[predict(model,s,xs) for s,xs in test]
  for mode,pred in [('stateless_baseline',stateless),('transition_learning',recurrent),('recurrent_state_model',recurrent)]:
   rows.append(dict(trial=trial,seed=seed,mode=mode,train_sequences=len(train),heldout_sequences=len(test),heldout_behavior_accuracy=score(pred,truth)))
 raw=out/'OMEGA-SEQUENCE-MEMORY-TRANSFER-2026-10-12.csv'
 with raw.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 summ=[]
 for mode in MODES:
  v=[x['heldout_behavior_accuracy'] for x in rows if x['mode']==mode]
  summ.append({'mode':mode,'trials':TRIALS,'mean_accuracy':statistics.mean(v),'sd':statistics.pstdev(v),'min':min(v),'max':max(v)})
 js=out/'OMEGA-SEQUENCE-MEMORY-TRANSFER-2026-10-12-summary.json'
 js.write_text(json.dumps({'experiment':'Sequence-dependent memory and held-out behavior','hidden_rule':'two-state recurrent machine: next_state = current_state XOR input','training_sequences_per_trial':40,'training_lengths':[2,6],'heldout_sequences_per_trial':50,'heldout_lengths':[7,12],'trials':TRIALS,'rows':len(rows),'summary':summ},indent=2)+'\n')
 print('ROWS',len(rows),'CSV_SHA256',hashlib.sha256(raw.read_bytes()).hexdigest(),'SUMMARY_SHA256',hashlib.sha256(js.read_bytes()).hexdigest())
 for x in summ:print(x)
if __name__=='__main__':main()
