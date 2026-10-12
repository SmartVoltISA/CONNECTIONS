# Ω-Stand — Fixed-budget repair and functional continuity

- Date: 2026-10-12
- Status: **PILOT RESULT — SOURCE COMMITTED; RAW CSV GENERATED LOCALLY BUT NOT YET COMMITTED**
- Code: [omega_fixed_budget_repair.py](./omega_fixed_budget_repair.py)
- Related prior record: [connectivity recovery pilot](./OMEGA-WHOLE-PARTS-CONNECTIVITY-PILOT-2026-10-11.md)

## Preregistered question

With only two new edges available after damage, does selecting bridges according to task reachability preserve function better than choosing bridges at random?

## Design

- 60 nodes; 150 initial undirected edges sampled uniformly.
- 45% of initial edges independently removed.
- 8 source-target task pairs chosen before damage per trial.
- 200 trials; seeds 20261012–20261211.
- Three paired modes: no repair, random bridge repair, task-aware bridge repair.
- Both repair strategies have a fixed budget of 2 edges; if no cross-component pair remains, fewer edges may be used.
- After measuring repair, apply a second 10% edge-loss event and measure task reachability again.
- Metrics: fraction of task pairs still connected; largest-component fraction; number of components; repair edges used.
- Task-aware selection greedily maximizes newly connected task pairs, then component-size product, then endpoint degree sum. This is a defined heuristic, not a claim of globally optimal repair.

## Actual Python results (200 paired trials)

| Metric (mean) | No repair | Random bridge | Task-aware |
|---|---:|---:|---:|
| Task-pair reachability after repair | 0.8506 | 0.9144 | 0.9819 |
| Task-pair reachability after second damage | 0.7856 | 0.8463 | 0.9150 |
| Largest component after repair | 0.9233 | 0.9595 | 0.9618 |
| Largest component after second damage | 0.8888 | 0.9229 | 0.9266 |
| Mean new edges added | 0.00 | 1.88 | 1.88 |

Paired differences in task reachability, mean difference with approximate 95% t interval:

| Contrast | After repair | After second damage |
|---|---:|---:|
| Task-aware − random | +0.0675 [0.0549, 0.0801] | +0.0688 [0.0532, 0.0844] |
| Random − no repair | +0.0638 [0.0526, 0.0749] | +0.0606 [0.0437, 0.0776] |
| Task-aware − no repair | +0.1313 [0.1168, 0.1457] | +0.1294 [0.1113, 0.1475] |

These intervals are descriptive paired t intervals, not a substitute for independent rerun and broader robustness checks.

## Interpretation

1. Under this synthetic task, task-aware edge placement preserved more of the eight designated source-target routes than random bridge placement at the same maximum budget.
2. The difference is larger for task reachability than for largest-component fraction. This supports measuring function, not only global connectivity.
3. The advantage persisted after an additional random edge-loss event in this particular model.
4. This does not establish a universal Ω law. The task-aware heuristic is explicitly optimized for the chosen task pairs, so its advantage is partly expected by design. Different tasks, graph distributions, damage patterns, and costs must be tested.
5. The result concerns restoration of preselected pairwise reachability. It does not yet demonstrate emergence of new modules or a new level of organization.

## Decision

**Limited positive result for task-aware repair in this benchmark.** Preserve as an experimental lead, not a universal principle.

## Reproducibility status

The Python standard-library script is committed. It generates per-trial CSV and aggregate JSON when run locally:
```bash
python experiments/omega_fixed_budget_repair.py --out omega-stand-results
```
The actual run produced 600 mode-trial rows (200 trials × 3 modes). The raw CSV and generated JSON are not yet committed alongside this report; the result remains provisional until those outputs are archived and the script is independently rerun.
