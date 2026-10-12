# Ω Dual-Contour Benchmark — 2026-10-12

## Research question
Does routing known situations to a fast cached contour and unknown situations to an exploratory contour improve the accuracy/cost trade-off?

## Hypothesis
The hybrid should match exploratory accuracy while spending less query budget, because known tasks bypass calibration. Fast-only should be cheaper but less accurate on unseen tasks.

## Null hypothesis
Hybrid has no accuracy/cost advantage over the best single-contour baseline.

## Preregistered setup
- 100 trials; seed for trial i is 20261013+i.
- Each task is a deterministic four-entry binary lookup table.
- 8 known tasks are cached; 4 novel tasks are not.
- Every architecture evaluates all four input cases for each task.
- Calibration of a novel task costs four extra observations; total cost is calibration plus evaluation.
- Modes: fast_only, exploratory_only, hybrid.
- Metrics: exact accuracy, total query cost, novel rules discovered.

## Important limitation
The four-entry rule is completely revealed by four calibration observations. Thus this benchmark checks routing and cost accounting, not open-ended discovery or general reasoning. No conclusions about consciousness or general intelligence follow.

## Reproduction
```bash
python experiments/omega_dual_contour_benchmark.py --out results --trials 100
```

## Execution record
A JavaScript reference simulation was run in the current session with 100 deterministic trials (300 mode/trial rows). The Python reproduction script and protocol are committed here; the summary values below come from the reference simulation, not from a claimed Python execution.
