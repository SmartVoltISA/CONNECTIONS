# Verified result: topology and dynamics

Model:
- N=8 binary nodes
- E=12
- degree=3
- synchronous local rule f(self_state, active_neighbor_count)
- 256 rules
- 256 initial states per rule
- 393,216 trajectories across six non-isomorphic 3-regular graphs

Verified graph statistics:

| Graph | connected | triangles | clustering | lambda2 | diameter | hetero rules | fixed hetero | multi-attractor | avg max cycle | max cycle |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| G0 | no | 8 | 1.000 | 0 | — | 238 | 222 | 238 | 3.046875 | 12 |
| G1 | yes | 4 | 0.500 | 0.763932 | 3 | 244 | 238 | 248 | 6.554688 | 28 |
| G2 | yes | 2 | 0.250 | 1.267949 | 3 | 240 | 238 | 248 | 11.218750 | 43 |
| G3 | yes | 1 | 0.125 | 1.438447 | 2 | 244 | 235 | 248 | 7.886719 | 30 |
| G4 | yes | 0 | 0.000 | 2.000000 | 3 | 246 | 236 | 248 | 3.492188 | 10 |
| G5 | yes | 0 | 0.000 | 2.000000 | 2 | 240 | 236 | 248 | 7.265625 | 32 |

Definitions:
- hetero: at least one attractor contains a state other than all-0/all-1.
- fixed hetero: at least one heterogeneous fixed-point attractor.
- multi-attractor: more than one distinct attractor.

Important control:
G4 and G5 have the same N, E, degree, zero triangles, zero clustering and
lambda2=2, but different cycle statistics. Therefore lambda2 alone is not a
complete predictor of the observed dynamics.

Connected-graph correlations were not treated as strong statistics because
there are only five connected graph classes.

Conclusion:
Within this model, topology changes global dynamics. This is a model-specific
result, not a universal law.
