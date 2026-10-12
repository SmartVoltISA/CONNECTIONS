# Ω Generalization Sweep — 2026-10-12

## Status
Actual Python execution completed. The full sweep ran twice independently; CSV and JSON summary were byte-identical between runs.

- Raw CSV rows: 1,620 (18 configurations × 30 trials × 3 modes)
- Graph families: Erdős–Rényi-like random graph and modular graph (6 communities)
- Damage to initial graph: 25%, 45%, 60%
- Repair budgets: 1, 2, 4 edges
- Modes: no repair, random bridge, task-aware bridge
- Each trial: 8 designated training pairs and 8 separately sampled held-out pairs
- After repair: an additional random loss of 10% of the remaining edges
- Node count: 60; initial edges: 150

## Main result
Task-aware repair consistently improves the training-pair metric in several damaged configurations, but this advantage does **not** reliably transfer to held-out pairs. Across the 18 graph/damage/budget configurations, task-aware minus random-bridge held-out reachability after repair ranged from -0.0458 to +0.0583; after the second damage it ranged from -0.0250 to +0.0625. Thus there is no universal winner in this sweep.

Selected configuration (45% damage, budget 2):
- ER: task-aware training reachability 0.992 vs random 0.921; held-out 0.958 vs random 0.975; held-out after second damage 0.900 vs random 0.921.
- Modular: task-aware training 1.000 vs random 0.975; held-out 0.958 vs random 0.971; held-out after second damage 0.912 vs random 0.938.

## Interpretation / limitations
This is evidence about a specific synthetic graph-repair benchmark, not a universal law of system organization and not evidence of emergence of new organizational levels. Task-aware selection directly optimizes the training pairs, so training gains can reflect metric overfitting. The 8 held-out pairs are a small sample; only two graph families, three damage levels, three budgets, and one secondary-damage rule were tested. The additional damage is deterministic by seed but samples the sorted edge set separately for each strategy; it is not an edge-by-edge identical intervention when repaired edge sets differ.

## Reproduction
Run with Python 3 (standard library only):
```bash
python experiments/omega_generalization_sweep.py --out results
```

## Local verification
- Raw CSV SHA-256: `58e049473886a08f17498ed7e65a2a9eb1476fa8d0787a355131284d74d6c361`
- Summary JSON SHA-256: `08b30e7a8f84b93d677a47e10fb05e3513a7b300c273a84bd18ab9cf9c3d1bad`
- Both files matched byte-for-byte on a second execution.
- Raw CSV was generated in the execution environment; this report does not claim the raw CSV has been committed to the repository.
