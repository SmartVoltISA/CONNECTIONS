# Ω-EXP — Repair-strategy comparison (negative design result)

- Date: 2026-10-11
- Status: **NEGATIVE / NON-DISCRIMINATING DESIGN**
- Related record: [Ω whole-parts connectivity pilot](./OMEGA-WHOLE-PARTS-CONNECTIVITY-PILOT-2026-10-11.md)

## Question
Does component-aware or degree-aware bridge placement improve structural outcomes over random bridge placement under equal repair budget?

## Actual pilot run
Python execution: 200 trials; N=60; 150 initial undirected edges; independently remove 45% of initial edges; seeds 20261111 through 20261310. Each strategy receives a bridge budget equal to the number of components after damage minus one.

| Strategy | Mean largest-component fraction | Mean component count | Mean edges added |
|---|---:|---:|---:|
| No repair | 0.93067 | 4.725 | 0 |
| Random bridge | 1.00000 | 1.000 | 3.725 |
| Size-aware bridge | 1.00000 | 1.000 | 3.725 |
| Degree-proxy bridge | 1.00000 | 1.000 | 3.725 |

## Interpretation
This design cannot distinguish the three repair strategies on the chosen metrics: all strategies are explicitly given enough edges to connect every component, and component count / largest-component fraction become identical by construction. This is a useful negative methodological result, not evidence that strategies are equivalent in general.

The "degree-proxy" strategy is not true modularity optimization. No claim about emergent modules is supported.

## Decision
Do not promote a structural principle from this test. Redesign the next experiment so the repair budget is fixed independently of damage (e.g. exactly 1 or 2 edges per trial), or measure functional reachability, repair cost, robustness under a second damage event, and modularity with pre-registered metrics. Preserve no-repair as negative control.

## Evidence limitation
Aggregate results are preserved here. Per-trial raw output and executable source were not archived as part of this record; certification remains blocked until a script and raw output are committed and rerun from the repository.
