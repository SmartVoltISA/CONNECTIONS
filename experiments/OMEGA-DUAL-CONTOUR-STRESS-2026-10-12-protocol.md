# Ω Dual-Contour Stress Test — protocol

Date: 2026-10-12

## Question
Does shared memory help a hybrid system combine fast recall with exploratory prediction under noisy training observations and a mid-episode rule change?

## Hypothesis
The hybrid with shared memory will adapt more effectively after the rule change than the hybrid without shared memory. Fast-only will have low coverage when training has not observed a state/input pair.

## Fixed design
- 300 trials by default; seed = 20261013 + trial index.
- Four-state affine transition: next = (a*state + b*input + c) mod 4.
- Training has 6–10 transitions with 15% corrupted observed labels.
- Test has 100 transitions; rule changes after transition 50.
- Modes: fast-only cache, exploratory model, hybrid with shared memory, hybrid without shared memory.
- The true next state is revealed after each prediction. The shared-memory hybrid writes that feedback to its cache.
- Metrics: overall accuracy, pre/post-shift accuracy, cache hits, exploration calls, abstentions.

## Guardrails
This is a finite synthetic environment. Feedback after each prediction is a strong supervision assumption. Results do not establish autonomous discovery, general intelligence, or consciousness.

## Reproduction
```bash
python experiments/omega_dual_contour_stress.py --out results --trials 300
```
