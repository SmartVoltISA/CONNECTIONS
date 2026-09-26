# Minimal relation experiments

This directory contains the earliest connection-related tests.

## Neutral finite dynamics

For deterministic functions f:S→S, exhaustive enumeration was performed for N=1..6 states:

N=1: 1 system
N=2: 4
N=3: 27
N=4: 256
N=5: 3125
N=6: 46656

Verified counts:

| N | cycles >=2 | proper invariant subset | nontrivial transition |
|---|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 3 | 3 |
| 3 | 11 | 25 | 26 |
| 4 | 131 | 250 | 255 |
| 5 | 1829 | 3101 | 3124 |
| 6 | 29849 | 46536 | 46655 |

Interpretation: two states are sufficient for nontrivial deterministic dynamics.
This does not prove that a separately named "relation" is a primitive.
