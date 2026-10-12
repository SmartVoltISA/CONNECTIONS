# Ω Dual-Contour Benchmark — 2026-10-12

## Status
Executed in Python in this session: 300 deterministic trials, 900 result rows. The experiment script and summary JSON are committed. The raw CSV was generated for the run but is not committed.

## Question
Does a hybrid of a fast cache and an exploratory model retain exploratory accuracy while reducing repeated exploratory calls?

## Protocol
- Environment: 4-state deterministic transition system, hidden rule `next = (a × state + b × input + c) mod 4`; each coefficient is in `{0,1,2,3}` (64 candidate rules).
- Each trial chooses a hidden rule, provides 5–9 observed transitions, then evaluates on a fresh 120-step trajectory.
- `fast_cache`: predicts only transitions seen during training; otherwise abstains.
- `exploratory_model`: enumerates the finite rule class, keeps rules consistent with training, and deterministically selects the first consistent rule.
- `hybrid`: uses the cache when available; otherwise uses the exploratory rule. It adds a transition to its cache only when observed feedback confirms its prediction.
- Seeds: 20261012–20261311. All modes are evaluated on the same generated trial.

## Results

| Mode | Mean accuracy | SD across trials | Mean exploratory calls / 120 | Mean cache uses | Mean abstentions |
|---|---:|---:|---:|---:|---:|
| Fast cache | 43.85% | 23.38 pp | 0.00 | 52.62 | 67.38 |
| Exploratory model | 93.29% | 24.64 pp | 120.00 | 0.00 | 0.00 |
| Hybrid | 93.29% | 24.64 pp | 15.02 | 104.98 | 0.00 |

Hybrid made about **87.5% fewer exploratory calls** than exploratory-only (15.02 vs 120 per test trajectory) while matching mean accuracy in this benchmark. Fast-cache accuracy counts abstentions as incorrect; its coverage was 52.62/120 transitions on average.

## Interpretation and limits
This supports a narrow engineering result: with feedback and a cache, a hybrid can reuse successful predictions and reduce repeated model calls on this toy task. It does not show that an emergent contour can discover arbitrary rules, that it is conscious, or that it generalizes to real-world semantics.

Important confound: the hybrid receives feedback after every transition and only caches a prediction when it is correct. The exploratory model uses a tiny hand-specified hypothesis class and resolves ambiguity by selecting the first consistent candidate. A stronger follow-up should charge explicit costs for hypothesis search, test noisy observations and regime changes, and compare against a hybrid whose cache updates require repeated independent confirmation.

## Reproduction
```bash
python experiments/omega_dual_contour_benchmark.py --out results --trials 300
```

CSV SHA-256: `71dc8d9805ad16a2068a4d5fa98d5961173abc9b13635814f2e08bc487722f15`

Summary JSON SHA-256: `73933102d6cc8a0ad7c371d78931ec36295817d833c01d97ee1cbea5496274b6`
