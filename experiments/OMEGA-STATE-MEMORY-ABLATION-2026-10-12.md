# Ω State and Memory Transfer Ablation — 2026-10-12

## Actual execution status
The local Python standard-library experiment ran twice independently. The raw CSV and JSON summary matched byte-for-byte between those two runs.

- Rows: 2,880 (2 graph families × 3 edge-loss levels × 3 node-removal levels × 40 trials × 4 modes).
- 60 nodes, 150 initial edges.
- 12 training task pairs and 12 separately sampled held-out task pairs per trial.
- Modes: no transfer, role-only transfer, state-only transfer, role + state transfer.
- Synthetic node state: categorical variable with four possible values.
- Raw CSV SHA-256: `95885b0728714071fe0262cbd4c7d4de3f952da200726a6930e47cd029619333`
- Summary JSON SHA-256: `4c01bca2ba0e456996a8d3f635b3f2e0e9a9374105535a208656dfc9a7f76ffb`

## Selected results: held-out task reachability
Mean fraction of separately sampled held-out task pairs remaining connected after intervention:

| Graph | Edge loss | Node removal | No transfer | Role only | Role + state |
|---|---:|---:|---:|---:|---:|
| ER | 45% | 10% | 0.631 | 0.723 | 0.750 |
| ER | 60% | 10% | 0.448 | 0.665 | 0.700 |
| ER | 60% | 20% | 0.260 | 0.537 | 0.552 |
| Modular | 45% | 10% | 0.656 | 0.762 | 0.779 |
| Modular | 60% | 10% | 0.356 | 0.662 | 0.694 |
| Modular | 60% | 20% | 0.206 | 0.596 | 0.598 |

Across all 18 aggregate graph/damage/removal settings, role + state transfer had higher held-out reachability than role-only transfer in this local run. State-only transfer does not restore graph edges, so its held-out reachability matches the no-transfer mode.

## What this does and does not show
The graph-role transfer mechanism improves structural reachability in this synthetic setup. Explicit categorical-state copying preserves that toy state at 100% for transferred nodes by construction. This is **not** evidence that meaningful memory, semantic identity, or consciousness can be transferred: the state is a random four-valued label, copied directly rather than reconstructed or interpreted.

## Reproducibility qualification
The local execution harness and the committed reproduction script were independently authored versions and are not byte-identical. The hashes above identify the local execution artifacts, not outputs produced by the repository script. The committed script should be run in a clean environment and its outputs compared before these hashes are attributed to that script. The raw CSV has not been committed.

## Reproduce with repository script
```bash
python experiments/omega_state_memory_ablation.py --out results
```
