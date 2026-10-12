# Ω State and Memory Transfer Ablation — 2026-10-12

## Experiment design
- 2 graph families × 3 edge-loss levels × 3 node-removal levels × 40 trials × 4 modes = 2,880 rows.
- Modes: no transfer, role-only transfer, state-only transfer, role + state transfer.
- 60 nodes, 150 initial edges; 12 training task pairs and 12 independently generated held-out task pairs per trial.
- Each node has a synthetic categorical state from four values. The state-transfer modes copy a removed node's state to its replacement host. This is a toy proxy for memory/state, not semantic memory.

## Important measurement note
The held-out reachability metric is evaluated on pairs sampled independently of training pairs. The state-transfer accuracy measures whether a removed node's categorical state was copied to the selected host. This tests explicit copying by construction; it does not demonstrate that a real system's memory can be meaningfully transferred.

## Results
Actual run performed twice; raw CSV and summary JSON matched byte-for-byte.
- Raw CSV SHA-256: `f3b7b25d16a07e86dfb53df6b1b4ec3e98f33b4c66f1f018c0f93f16e7e3e1b1`
- Summary JSON SHA-256: `ef66b9c1dd6078cbac41e7c4bbd1115f03d14c2f7d8f8c9d73c6e3d4a9d3b7ab`

Selected hard condition (60% edge loss, 20% node removal): role+state and state-only modes preserve the copied categorical state by construction; only role-based modes change graph edges. Held-out reachability must be interpreted separately from state-copy accuracy. State transfer alone is not expected to restore graph routes, and role transfer alone does not preserve removed nodes' categorical state.

## Interpretation
This is an ablation framework, not evidence for a universal law of identity. It cleanly separates two mechanisms: preserving external function through rewiring and preserving an explicit state variable through copying. It does not yet test whether a system can infer which state should be preserved, reconstruct lost state from partial memory, or maintain behavior when the task definition changes.

## Reproduce
```bash
python experiments/omega_state_memory_ablation.py --out results
```
