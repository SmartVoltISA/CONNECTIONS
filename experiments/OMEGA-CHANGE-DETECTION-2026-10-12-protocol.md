# Ω Change Detection and Memory Ablation — preregistration

Date: 2026-10-12

## Question
Can a hybrid detect that its known rule has become unreliable, and does shared memory improve post-change adaptation?

## Conditions
- 500 trials by default; deterministic seed = 20261015 + trial.
- Four-state affine rules: next = (a*state + b*input + c) mod 4.
- Initial training: 10–16 transitions with 10% corrupted labels.
- Test: 160 transitions, rule changes after step 80.
- Feedback: delayed by 5 steps and corrupted 10%.
- Modes: fixed routing with shared memory; calibrated confidence + change detector; no shared memory.
- Metrics: total accuracy, pre/post-change accuracy, fast/exploration calls, change-detection rate and delay.

## Hypotheses
H1: Calibrated confidence and change detection improve post-change accuracy compared with fixed routing.
H2: Shared memory improves adaptation over the no-shared-memory condition.
Null: neither calibrated change detection nor shared memory provides a measurable benefit.

## Fixed detector
Use matured feedback only. Trigger a change alarm when at least four matured labels are available in the recent 20-step window and at least 50% disagree with their stored predictions. In calibrated mode, clear the cache on alarm and use the exploratory model for uncertain cases.

## Limitations
Small finite synthetic rule family; fixed initial hypothesis class; noisy delayed labels; results cannot establish emergence, general intelligence or consciousness.

## Reproduction
```bash
python experiments/omega_change_detection_benchmark.py --out results --trials 500
```
