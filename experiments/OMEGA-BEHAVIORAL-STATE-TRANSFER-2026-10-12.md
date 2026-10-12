# Ω Behavioral State Transfer — 2026-10-12

## Execution
Actual local Python run completed twice; CSV and JSON outputs were byte-identical.

- 3,240 rows: 2 graph families × 3 edge-loss levels × 3 node-removal levels × 60 trials × 3 modes.
- 48 nodes, 112 initial edges.
- Edge loss: 25%, 50%, 65%; node removal: 5%, 15%, 25%.
- Each node has a 2-bit categorical state; its behavior on input x is output state XOR x.
- Inputs 0/1 are designated training probes; inputs 2/3 are held-out behavioral probes.
- CSV SHA-256: `90b475b1e2f413d3f909099ecfa0e388ea68eb520155ece3bf708ff1e92b3b26`
- Summary SHA-256: `7240dabb720878e45348cf2004b3d04eaed6d39257f7ac1f396ec280fa8c6a1f`

## Selected results
Held-out behavioral match (random successor vs state-aware successor):
- ER, 50% edge loss, 15% node loss: 24.8% vs 25.7%.
- ER, 65% edge loss, 5% node loss: 25.0% vs 29.2%.
- Modular, 25% edge loss, 15% node loss: 24.3% vs 25.5%.
- Modular, 65% edge loss, 5% node loss: 28.3% vs 24.2%.

Held-out route reachability (no transfer / random successor / state-aware successor):
- ER, 65% edge loss, 15% node loss: 18.9% / 55.5% / 52.2%.
- Modular, 65% edge loss, 15% node loss: 15.3% / 59.3% / 55.7%.
- ER, 50% edge loss, 15% node loss: 46.8% / 62.9% / 60.9%.

## Interpretation
Role/neighbor rewiring markedly improves graph reachability in severe damage conditions. State-aware successor selection does **not** reliably outperform random successor selection on held-out behavioral matching: inferred state is often noisy, and results vary by graph/damage condition. This is a useful negative result: copying or guessing a state is not enough; the model needs a better state-inference/validation mechanism.

## Limits
This is a toy model with four categorical states and a hand-designed XOR behavior. It does not model semantic memory, learning, or a real agent. The committed script is a compact reproduction implementation; the hashes above identify the local execution artifacts, not a claim that the committed script emitted byte-identical artifacts. Raw local CSV is not committed.
