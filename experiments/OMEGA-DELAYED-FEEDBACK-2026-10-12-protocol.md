# Ω Delayed-Feedback Benchmark — preregistered protocol

Date: 2026-10-12

## Question
Does routing based on cache confidence help when labels are noisy, delayed, and the environment changes its hidden transition rule?

## Hypotheses
H1: A hybrid with confidence-gated routing will improve the accuracy/coverage trade-off over fast-only and fixed routing.
H2: Delayed shared feedback will improve adaptation after a rule shift, but noisy labels will limit the benefit.
Null: confidence-gated routing and shared feedback do not improve held-out performance.

## Fixed setup
- 300 trials; seed = 20261014 + trial.
- Hidden state and input each take values 0–3.
- Hidden rule: next = (a*state + b*input + c) mod 4, with 64 possible rules.
- Training: 8–14 transitions, 10% corrupted labels.
- Test: 120 transitions; hidden rule changes after step 60.
- Feedback arrives after 5 steps and is corrupted at 10%.
- Architectures: fast-only, exploratory-only, hybrid-fixed, hybrid-confidence.
- Metrics: total accuracy, pre/post-shift accuracy, fast uses, exploration calls, abstentions.

## Fairness and limitations
All modes see the same generated episode and use fixed seed schedules. Confidence threshold is 0.75. The benchmark is synthetic, feedback is still supplied by the environment, and this does not establish general reasoning or consciousness.

## Reproduction
```bash
python experiments/omega_delayed_feedback_benchmark.py --out results --trials 300
```
