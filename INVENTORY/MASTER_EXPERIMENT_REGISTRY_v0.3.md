# CONNECTIONS — MASTER EXPERIMENT REGISTRY v0.3

Generated: 2026-09-26
Status: ACTIVE / CLASSIFICATION PASS 3
Purpose: normalized registry of unique experiment lineages. This version incorporates the additional physical-control and Ω-TEST records verified directly in Ω-Lab.

## 1. Counting rule

Count a unique experimental lineage only when there is a distinct research question/protocol identity. Do NOT count:
- source/result copies;
- scripts belonging to the same experiment;
- audits of the same experiment;
- CI jobs;
- result files as experiments;
- superseded files as independent confirmations.

Corrected replications remain separate lineages when the protocol/model was materially corrected.

## 2. Verified family map

| Family | Verified unique blocks | Classification |
|---|---:|---|
| Ω-MEM | 11 named blocks: MEM-1, 1a–1d lineage, 2, 3, 4, 4R, 5, 6, 7, 8, 9 + MEM-TIME | mixed research/replication |
| Ω-INF | 8 | experimental family |
| Ω-B | 6 | hypothesis/control sequence |
| Ω-LINK-1 | 1 | one family, many result artifacts |
| Ω-BASIS-002 | 1 base lineage + R1/R2 replications | replication lineage |
| Ω-EMO-001A | 1 + R1 | validated within tested scope |
| Ω-REL early | multiple numbered relation lineages | requires lineage normalization |
| REL-66…73 | 8 later black-box/blind blocks | distinct later family |
| Ω-TIME | 9 experimental blocks: 001,002,003–005,006,007,008,009,010,011 | 003–005 is one combined block |
| E-ENERGY | 25+ named records including 0010–0013, 0020–0037, 0032R and dedicated hysteresis/Preisach/symmetric-bifurcation records | result-by-result audit required |
| E-LIGHT | 6 verified records: 0001–0005, 0007 | exploratory/toy models |
| E-AC | 2 | physical/model controls |
| E-MAGNETIC | 1 ID but two same-ID records exist with different questions; identity conflict must be resolved before counting | unresolved identity |
| E-MOTION | 2 | exploratory/control |
| E-ENVIRONMENT | 1 | inventory/experimental preparation |
| Ω-TEST | 10 verified primary experiment records: 1,2,3,4,5,7,9,10,11,12 | mixed exploratory/falsification |
| PHYS-ELECTRON | 5-stage lineage: 002,002A,003,004,005 | corrected/superseded stages present |
| CICADA | 6: C1-002,015,016,017,018,019 | separate research branch |
| Ω-RH | RH-01…64 research/attack/audit sequence, not 64 experiments by default | mathematical research branch |
| FOUNDATION / D-R-W-P | multiple research objects; neutral-machine execution exists | not yet one-count-per-file |
| ORISIK canonical | 20 registry-level records, with several source/research copies | separate organism evidence layer |

## 3. Directly verified Ω-TEST status

- TEST-1: completed reproducible analytic/geometric check.
- TEST-2: completed analytic + numerical geometric check.
- TEST-3: completed exploratory numerical test.
- TEST-4: completed exploratory numerical interaction test.
- TEST-5: completed after numerical-stability correction.
- TEST-7: first run invalidated because of non-finite scores; corrected 180-dataset blind rerun completed. The failed first run remains historical evidence, not a second successful experiment.
- TEST-9: completed matched-marginal counterfactual test.
- TEST-10: completed but failed as a validated effect metric.
- TEST-11: completed exploratory numerical counterfactual test.
- TEST-12: completed exploratory cross-family falsification test.

The existence of TEST-1…12 does not imply that all intermediate numbers are present as separate experiments. Missing IDs are not silently invented.

## 4. Directly verified physical-control branch

### E-LIGHT
E-LIGHT-0001 through 0005 and 0007 are separate named records. They are explicitly described as exploratory/toy-model work; they do not establish physical laws or spontaneous emergence of exactly three classes.

### E-AC
E-AC-0001 and E-AC-0002 are separate controls. E-AC-0002 tests energy exchange in an RLC model and supports the narrower statement that zero of one observable/channel does not imply zero total stored state.

### E-MOTION
E-MOTION-0001 is a hypothesis/synthesis layer; E-MOTION-0002 is a numerical topology control. Do not treat both as equivalent validated physical experiments.

### E-ENVIRONMENT
E-ENVIRONMENT-0001 is primarily a real-gradient inventory/preparation object. It should not be counted as an executed physical experiment without an execution record.

### E-MAGNETIC
Two different files carry the same ID E-MAGNETIC-0001 but ask materially different questions:
1. magnet + coil flux/motion/energy cycle;
2. environmental potential / lightning analog.
They must remain separate records until provenance resolves whether one is a renamed/replaced version or an accidental ID collision.

## 5. Important evidence corrections

- Ω-MEM-4 remains exploratory/not validated.
- Ω-MEM-4R is a corrected replication, not a duplicate.
- Ω-TEST-7's failed unstable run is not counted as a successful independent experiment.
- ELECTRON-003 is not independent confirmation of corrected ELECTRON-004.
- Ω-RH steps are not automatically empirical experiments.
- CI success does not upgrade a scientific claim.
- Application registry claims remain downstream of experiment-level evidence.

## 6. Current safe count statement

A single final TOTAL is still not frozen in v0.3 because three classes of ambiguity remain:
1. early Ω-REL numbered records need exact protocol/execution lineage;
2. E-ENERGY has result records and dedicated branch records that need identity reconciliation;
3. E-MAGNETIC-0001 has an explicit ID collision.

What IS now safe to state is that the project contains **well over 50 distinct named experimental/research blocks**, and the normalized count is substantially below the 629 raw files. A precise final number must be produced from the lineage table, not inferred from filename counts.

## 7. Required final ledger

For every record:

`ID | family | question | protocol | implementation | execution | result | control/audit | replication | final status | SHA | related IDs`

Allowed status:
PLANNED | CODED | EXECUTED | VALIDATED | REPRODUCED | REJECTED | INVALIDATED | SUPERSEDED | UNKNOWN

## 8. Decision

v0.3 is the first registry version where the physical controls and Ω-TEST primary records are explicitly separated from their supporting files.

The next operation is mechanical rather than conceptual:
resolve the three ambiguity classes above, then emit the final ledger and counts by status.
