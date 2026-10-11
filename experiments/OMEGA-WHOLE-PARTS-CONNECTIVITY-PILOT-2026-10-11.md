# Ω-EXP — Whole ↔ Parts: connectivity recovery pilot

- Record date: 2026-10-11
- Status: **PILOT / NOT A CERTIFIED RESULT**
- Repository role: CONNECTIONS experiment record; canonical principle remains in SYSTEM-FOUNDATION.
- Question: after random edge damage, does topology repair restore global connectivity more effectively than changing weights on surviving edges only?
- Hypothesis: adding edges across disconnected components restores graph connectivity; weight reinforcement without adding edges cannot reconnect disconnected components.
- Null / baseline: topology remains unchanged after damage.
- Model: undirected Erdős–Rényi-like graph sampled uniformly from all possible edges; N=60 nodes; 150 initial edges; 45% of initial edges independently removed; 200 paired trials; seeds 20261011 through 20261210.
- Metrics: largest connected component / N; number of connected components; number of repair edges.
- Paired design: A–D share each trial's same initial graph and damaged graph. Repair RNG is deterministic from the trial stream.
- Modes:
  - A: no topology repair.
  - B: add the minimum number of random bridge edges needed to connect components.
  - C: reinforce weights of surviving edges only; topology unchanged. (Weights do not affect the connectivity metric.)
  - D: same topology repair as B plus edge-weight reinforcement; because the primary metric is topological, the added weighting has no modeled effect on that metric.
- Implementation note: actual Python execution completed in this session. This record contains aggregate output, not a checked-in executable script; reproduction should be rerun from an archived script before certification.

## Results

| Metric | Mean | Population SD | Min | Max |
|---|---:|---:|---:|---:|
| Largest-component fraction after damage (A/C) | 0.92917 | 0.03631 | 0.78333 | 1.00000 |
| Largest-component fraction after repair (B/D) | 1.00000 | 0.00000 | 1.00000 | 1.00000 |
| Connected components after damage | 4.84 | 1.79008 | 1 | 11 |
| Connected components after bridge repair | 1.00 | 0.00000 | 1 | 1 |
| Added bridge edges | 3.84 | 1.79008 | 0 | 10 |

## Interpretation

1. In this deliberately simple graph model, bridge repair restored a single connected component in all 200 trials.
2. Weight reinforcement alone did not change topology, so it did not change the connected-component metrics.
3. D did not outperform B on the chosen metric. This is not evidence that feedback is generally useless: the experiment defined feedback as weight reinforcement and measured only topology.
4. The average post-damage largest component remained high (92.9% of nodes), so global connectivity alone may hide local fragmentation. Component count and functional reachability should also be measured.
5. This pilot does **not** test emergence of modules, preservation of function, adaptive edge selection, or the universal Ω principle. It tests only a narrow graph-connectivity claim.

## Decision

- Result class: **LIMITED PASS** for the narrow claim that adding bridge edges can reconnect components in this implementation.
- No promotion to a universal law.
- Next preregistered experiment: compare (i) random bridge repair, (ii) function-aware repair, and (iii) modularity-seeking repair under the same edge budget; measure component connectivity, modularity, targeted-task reachability, damage robustness, and repair cost. Include a negative control with no repair and retain per-trial raw data plus executable script.
- Evidence status: aggregate values were computed from 200 actual Python trials; raw per-trial rows and executable source are not yet archived in this repository. Certification blocked until those artifacts are saved and independently rerun.
