# Ω Functional Invariance — 2026-10-12

## Execution status
The Python standard-library experiment ran twice independently. The raw CSV and JSON summary matched byte-for-byte on the second run.

- 2,700 rows = 2 graph families × 3 damage levels × 3 turnover levels × 50 trials × 3 strategies
- 60 nodes, 150 initial edges
- Graph families: ER-like random and six-community modular
- Initial edge loss: 25%, 45%, 60%
- Edge turnover: 10%, 25%, 40% of remaining edges
- 12 designated source-target functions per trial
- Strategies: no repair, random rewiring, function-aware rewiring

## Results: function retention
Mean ratio of functions still reachable after rewiring/node-replacement proxy, relative to the intact initial graph:

| Graph | Initial damage | Turnover | No repair | Random rewiring | Function-aware |
|---|---:|---:|---:|---:|---:|
| ER | 25% | 10% | 0.978 | 1.000 | 0.999 |
| ER | 45% | 10% | 0.879 | 0.952 | 0.968 |
| ER | 45% | 25% | 0.895 | 0.937 | 0.918 |
| ER | 60% | 10% | 0.694 | 0.700 | 0.863 |
| ER | 60% | 25% | 0.685 | 0.708 | 0.756 |
| ER | 60% | 40% | 0.685 | 0.699 | 0.706 |
| Modular | 25% | 10% | 0.982 | 0.994 | 0.994 |
| Modular | 45% | 10% | 0.892 | 0.958 | 0.948 |
| Modular | 45% | 25% | 0.897 | 0.903 | 0.908 |
| Modular | 60% | 10% | 0.616 | 0.662 | 0.813 |
| Modular | 60% | 25% | 0.679 | 0.716 | 0.768 |
| Modular | 60% | 40% | 0.725 | 0.762 | 0.750 |

## Interpretation
The clearest pattern is conditional: under severe initial damage (60%), function-aware repair preserved more of the designated task reachability than the baselines in most tested settings. Under moderate damage, its advantage was mixed and sometimes absent. This supports investigating function-preserving repair, but does not establish a universal law.

Important limitation: the current “node replacement” stage is only a proxy. It keeps node IDs and reassigns the incident edges of selected nodes; it does not model semantic identity, hidden state transfer, or a truly new node taking over an old role. Also, task-aware repair is optimized against the same 12 tasks used for evaluation, so its gains are in-sample. A follow-up should use held-out functions, explicit role transfer, paired identical interventions, and multiple graph families.

## Reproduction
```bash
python experiments/omega_functional_invariance.py --out results
```

## Verification
- CSV SHA-256: `8c3468c4cdc48a8c70b6bb0dc9305718d26673872663c271441eeeccd77b057d`
- Summary JSON SHA-256: `efae415bed8b1fbee85cba2181488c842c896b3416fcb7ff54cf41102f2c6001`
- Raw CSV has 2,700 rows and was generated locally. It is not claimed as committed in this repository.
