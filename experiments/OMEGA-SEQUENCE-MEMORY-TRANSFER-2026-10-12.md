# Ω Sequence Memory Transfer — 2026-10-12

## Actual run
The local Python experiment ran twice independently; both CSV and summary outputs matched byte-for-byte.

- 80 independent trials, 40 training sequences and 50 held-out sequences per trial.
- Training sequence lengths: 2–6 inputs.
- Held-out sequence lengths: 7–12 inputs.
- Hidden behavior: a two-state recurrent machine, `next_state = current_state XOR input`.
- Total result rows: 240 (80 trials × 3 model variants).
- CSV SHA-256: `cb40159f147b8307b4cc43638d4dc9865c818fa26c4c8a00d289e74137268226`
- Summary SHA-256: `75e867370ef4fec0f5c7479d9a700752ac101193e4b155360448b7c52bf49407`

## Results

| Variant | Mean held-out behavior accuracy | Standard deviation |
|---|---:|---:|
| Stateless baseline (predict output = current input) | 49.81% | 2.33 pp |
| Learned transition table | 100.00% | 0.00 pp |
| Recurrent state model (same learned transition table) | 100.00% | 0.00 pp |

## Interpretation
The learned transition rule generalizes from short training sequences to longer unseen sequences in this deliberately simple deterministic task. The stateless baseline is near chance. This demonstrates that a minimal stateful rule can preserve sequence-dependent behavior beyond the observed sequences.

It does **not** show that an agent can infer or transfer complex semantic memory. The task has only two states and a simple XOR transition, and both learning variants use the same learned table; they are not independent algorithms. The 100% result is expected once all four state/input transitions have been observed, which occurred in these training traces.

## Next decisive test
Increase the hidden state space, use noisy/incomplete traces, withhold some state-input transitions during training, remove the original model, and let a successor infer the rule from partial history. Evaluate on novel long sequences and report confidence intervals. This will test generalization rather than table coverage.

## Reproduction
```bash
python experiments/omega_sequence_memory_transfer.py --out results
```

The raw CSV remains local and is not claimed to be committed to the repository. Hashes identify local execution artifacts; rerun the committed script to reproduce its own outputs.
