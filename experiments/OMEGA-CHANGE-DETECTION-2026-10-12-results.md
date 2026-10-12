# Ω Change Detection Benchmark — reference results

**Execution record:** 500 deterministic trials (1,500 mode/trial rows) were run in a JavaScript reference simulation during this session. The committed Python reproduction script was not executed here.

| Architecture | Overall accuracy | Before shift | After shift | Detection rate |
|---|---:|---:|---:|---:|
| Fixed routing + shared memory | 81.60% | 86.60% | 76.59% | — |
| Confidence + change detector | 34.59% | 43.94% | 25.24% | 99% |
| No shared memory | 49.73% | 74.95% | 24.52% | — |

## Important negative result
The confidence/change detector alarmed in 99% of trials, but on average about 49 steps **before** the actual rule change. Noisy initial observations triggered false alarms. The detector then cleared useful cached information and over-routed to the exploratory model. Its performance was substantially worse than fixed routing.

This rejects the current detector configuration; it does not reject change detection in general.

## Interpretation and next revision
1. Do not clear the cache on one alarm.
2. Require a sustained error increase against a calibrated pre-shift baseline.
3. Use a holdout stream or sequential change detector with a controlled false-alarm rate.
4. Report false alarms before the true shift, detection delay after the shift, and post-shift recovery separately.
5. Compare all modes with the same feedback and query budget.

## Limits
Finite synthetic affine rules, noisy delayed feedback, and a simple heuristic detector. This is not evidence of consciousness or general intelligence.
