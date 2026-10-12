# Ω Held-out Role Transfer — 2026-10-12

## Actual execution
Python standard-library simulation completed twice. Both CSV and summary JSON matched byte-for-byte.

- 648 trial-mode rows: 2 graph families × 3 edge-damage levels × 3 node-removal levels × 12 trials × 3 strategies.
- 60 nodes, 150 initial edges.
- 12 training task pairs used by the role-transfer strategy; 12 separately sampled held-out pairs used for evaluation.
- 25%, 45%, 60% edge loss; removal of 5%, 10%, 20% of nodes.
- Strategies: no repair, random role transfer, task-aware role transfer.
- CSV SHA-256: `d9cf839abcbd4ed1ee84ae17f8a8fa55e84169597d6e3251ffbcb22231bc157a`
- Summary SHA-256: `97ad52a71a5c52aad81af2ab352436387f17fdbe0541723866945ab34ea89f73`

## Held-out reachability after node removal and role transfer

Mean fraction of held-out task pairs that remain connected:

| Graph | Edge loss | Node removal | No repair | Random role transfer | Task-aware role transfer |
|---|---:|---:|---:|---:|---:|
| ER | 25% | 5% | 0.847 | 0.875 | 0.896 |
| ER | 45% | 5% | 0.757 | 0.785 | 0.826 |
| ER | 45% | 10% | 0.604 | 0.667 | 0.694 |
| ER | 60% | 10% | 0.438 | 0.674 | 0.708 |
| ER | 60% | 20% | 0.299 | 0.535 | 0.562 |
| Modular | 25% | 5% | 0.861 | 0.875 | 0.882 |
| Modular | 45% | 10% | 0.611 | 0.785 | 0.792 |
| Modular | 60% | 5% | 0.403 | 0.681 | 0.722 |
| Modular | 60% | 10% | 0.347 | 0.681 | 0.722 |
| Modular | 60% | 20% | 0.146 | 0.639 | 0.660 |

Across all 18 settings, task-aware role transfer had equal or higher held-out reachability than random role transfer in this run. This is a promising synthetic result, not proof of a universal law.

## Critical limitations
- Only 12 trials per configuration; uncertainty is substantial.
- Task-aware role transfer is selected using training pairs, while reported generalization is measured on held-out pairs; held-out results are not used for selection.
- “Role transfer” is a proxy: deleted nodes' surviving neighbors are attached to a surviving host. The model does not transfer hidden state, semantics, or internal memory.
- Node IDs are retained as graph positions, and some task endpoints may themselves be deleted; reachability then treats those endpoints as isolated.
- Only two graph families and this specific role-transfer rule were tested.

## Reproduce
```bash
python experiments/omega_heldout_role_transfer.py --out results
```
