# Ω Delayed-Feedback Benchmark — reference results

**Execution note:** The figures below come from a JavaScript reference simulation executed in this session (300 trials, 1,200 architecture/trial rows). The committed Python script is a reproduction artifact and was not executed here.

| Mode | Mean accuracy | Before rule shift | After rule shift | Mean exploration calls |
|---|---:|---:|---:|---:|
| Fast only | 32.04% | 52.11% | 11.98% | 0.00 |
| Exploratory only | 35.84% | 46.27% | 25.40% | 120.00 |
| Hybrid fixed routing | **78.53%** | **84.91%** | **72.15%** | 10.46 |
| Hybrid confidence-gated | 66.11% | 82.82% | 49.41% | 37.93 |

## Interpretation
The fixed hybrid did best in this reference run. The confidence-gated version performed worse, so the current confidence heuristic is not validated; it needs calibration and a fairer routing comparison. After the hidden rule changed, every mode lost accuracy, but the fixed hybrid retained the strongest performance in this toy environment.

## Limits
- Four-state synthetic affine rules only.
- Feedback labels were delayed by five steps and corrupted 10% of the time.
- A rule changed after step 60 of a 120-step episode.
- The JavaScript reference implementation and committed Python script have not been cross-validated for identical output.
- This is not evidence of consciousness or general intelligence.
