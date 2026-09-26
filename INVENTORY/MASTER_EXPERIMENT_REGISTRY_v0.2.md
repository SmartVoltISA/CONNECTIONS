# CONNECTIONS — MASTER EXPERIMENT REGISTRY v0.2

Generated: 2026-09-26
Status: ACTIVE / CLASSIFICATION PASS 2
Purpose: semantic reconciliation of Ω-Lab + ORISIK + ARCHIVE. This registry counts research lineages/experiment IDs, not files.

## 1. Evidence rule

`RESULT ≠ TRUTH`

`PROTOCOL → EXECUTION → RAW/DERIVED RESULT → AUDIT/CONTROL → CLASSIFICATION → REPLICATION`

A source file, numerical output, CI pass, or result filename is not execution evidence by itself.

## 2. Current inventory boundary

The raw source inventory contains 629 candidate files:
- Ω-Lab: 393
- ORISIK: 234
- ARCHIVE: 2

629 is NOT the experiment count. Candidate files include protocols, code, results, audits, controls, history, copies, indexes and non-experimental architecture.

## 3. Pass-2 semantic map

### Ω-MEM
Confirmed lineage blocks found:
- MEM-1 / 1a–1d
- MEM-2
- MEM-3
- MEM-4
- MEM-4R corrected replication
- MEM-5
- MEM-6
- MEM-7
- MEM-8
- MEM-9
- MEM-TIME

Important: MEM-4 and MEM-4R are separate lineage objects; MEM-4R is a corrected replication. MEM-4 remains exploratory/not validated because its implementation violated parts of the preregistered protocol. MEM-4R contains the corrected controlled comparison but its repository record explicitly says reported values are not independently rerun merely because they are recorded.

### Ω-INF
INF-1…8 identified.
These form one information/organization family with controls and robustness/falsification stages.
Do not count scripts, result files or controls as separate experiments.

Known result lineage:
- INF-3: bigram-preservation reconstruction
- INF-4: trigram-preservation reconstruction
- INF-5: independent-corpus replication
- INF-6: sampling-policy control
- INF-7: robustness
- INF-8: deliberate falsification/break test

### Ω-B
B0…B5 identified.
Current semantic classification:
- B0 initial hypothesis
- B1 execution/report
- B2 control
- B3 null-model test
- B4 preliminary comparison
- B5 proposed control, not executed

The family does not justify collapsing all six into one experiment or treating the entire branch as validated.

### Ω-LINK-1
One experiment family with multiple result/analysis artifacts, including RESULT-001…011, depth sweep, exhaustive horizon and distinguishability cross-checks.
Individual result files are not separate base experiments.
RESULT-017 is recorded as executed but not accepted as a substantive Ω result.

### Ω-BASIS
BASIS-002 plus R1/R2 lineage.
BASIS-002-R2 has numerical reproduction of the core result, but incomplete provenance/CI details prevent promotion to a universal/foundation claim.

### Ω-EMO
EMO-001A-R1 is a validated computational test within its stated CIE 1931 control scope.
Its result does NOT establish a universal claim about “three fundamental colors”; it establishes representation-specific rank/minimality for the tested mapping.

### Ω-REL / relation branch
Two layers must remain separate:
1. earlier OMEGA-REL research lineage (REL-001, 002A, 003, 004A/B, 005/006, 007, 009, 010, 011/012, 016, 018, 024, 029, 036, 041, 043, 045 and related records found);
2. later blind black-box lineage REL-66…73.

REL-66…73 are distinct later experiments/pilots, not duplicates of the earlier relation family.
REL-72 explicitly compares delay vs memory under blinded conditions; REL-73 removes predefined mechanism labels and tests unsupervised behavior discovery.

### Ω-TIME
Identified ID blocks:
- TIME-001
- TIME-002
- TIME-003–005 (one combined full temporal life-cycle experiment)
- TIME-006
- TIME-007
- TIME-008
- TIME-009
- TIME-010
- TIME-011

Thus the filename sequence contains 11 numeric IDs, but 003–005 is one combined experimental block and must not be inflated to three experiments without separate protocol/execution identity.

### ENERGY
Named records found include:
- E-ENERGY-0010…0013
- E-ENERGY-0020…0037
- E-ENERGY-0032R
- E-ENERGY-HYSTERESIS-BALANCE-001
- E-ENERGY-PREISACH-001
- E-ENERGY-0037-SYMMETRIC-BIFURCATION

The planned E-ENERGY-0001…0005 items in the ENERGY README remain planned/blocked and are not counted as executed experiments.
The ENERGY branch is explicitly hypothesis/open-research material; each result requires individual audit before application claims.

### PHYS-ELECTRON
Identified lineage:
- ELECTRON-002
- ELECTRON-002A verification
- ELECTRON-003 blind relation clustering
- ELECTRON-004 corrected blinded held-out relations
- ELECTRON-005 held-out process prediction / result branch

ELECTRON-003 is superseded by corrected ELECTRON-004 for the affected claim; they must not be counted as independent confirmations.

### CICADA-3301
Identified:
- EXP-C1-002
- EXP-C1-015
- EXP-C1-016
- EXP-C1-017
- EXP-C1-018
- EXP-C1-019

These are a separate research branch. Structural proof/control status must be kept distinct from interpretive meaning.

### Ω-TEST / REAL validation
TEST-1…12 are present as a sequence, with gaps/controls and later full-run references. A separate REAL validation protocol explicitly references TEST-11, TEST-12 and TEST-15; therefore TEST-15 in the mathematical index must not automatically be treated as a completed empirical experiment.
Known historical conclusions include failures of some universality/opposition claims. Do not promote them without the primary result record.

### Ω-RH
RH-01…64 are a research/attack/audit sequence, not 64 independent experiments by default.
The lineage contains mathematical constructions, computational tests, audits and rejected attacks. Verified examples:
- RH-31 attack rejected for the stated shift operator
- RH-32 replacement proposed, key lemmas unproved
- RH-33 finite Fourier-cutoff compact-resolvent result, without simplicity/limit/RH conclusion
- RH-34 naive Fourier-cone positivity rejected
No RH claim is established by this branch.

### MINIMAL BASIS / D-R-W-P
The branch contains an executed neutral-machine search and a D/R/W/P audit.
Current conclusion remains:
`D+R stronger than W+P = UNKNOWN / UNPROVEN`.
The next valid test is the primitive-emergence chain, while keeping symbolic labels separate from operational capability.

## 4. ORISIK

Canonical experiment registry currently contains:
- EXP-0001, EXP-0002
- EXP-0013…0018
- EXP-AUDIO-001…004
- EXP-VISION-001
- CL-SCALING-001, CL-SCALING-002
- SPACE baseline
- Ω-ANTI-BH v0.1 / EXPERIMENTS
- Ω-ANTI-BH v0.1 / LAB
- Ω-ANTI-BH v0.2
- MARKET EXP-0001, EXP-0002
- RELATIONAL-MEMORY-TEMPORAL-ORDER-001

B-Lab source copies and research records are one lineage where provenance proves identity.
Ω-ANTI-BH v0.1 EXPERIMENTS and LAB are RELATED, not EXACT_MATCH, because their blob SHAs differ.
CL-SCALING-001 has multiple execution/result/audit artifacts but remains one experiment lineage.
The registry's stale “execution pending” wording for CL-SCALING-001 is superseded by the actual execution/result artifacts found in the repository; primary evidence must be used for final status.

## 5. Provenance layers

ARCHIVE is treated primarily as provenance/history, not an automatic experiment source.
SPACE operational cycle records (PRESENT/PLAN/EXECUTION/VERIFICATION/FEEDBACK/CYCLE) are workflow objects unless a separate protocol establishes them as scientific experiments.

## 6. Current quantitative statement

At this pass we can safely report:
- 629 raw candidate files;
- dozens of distinct experiment families/branches;
- multiple tens of uniquely named experiment IDs/blocks;
- several hundred research artifacts after including results, controls, audits, code and history.

A single final “number of experiments” is intentionally NOT frozen yet because several ID sequences contain:
- combined blocks (e.g. TIME-003–005);
- corrected replications;
- superseded experiments;
- result-only files;
- mathematical attack/audit steps;
- source/result copies.

Freezing a number before lineage normalization would create a false precision.

## 7. Next canonical schema

Each unique lineage will become:

ID | family | question | protocol | implementation | execution evidence | result | control/audit | replication | status | source SHA | related IDs | CONNECTIONS edges

Status vocabulary:
PLANNED | CODED | EXECUTED | VALIDATED | REPRODUCED | REJECTED | INVALIDATED | SUPERSEDED | UNKNOWN

## 8. Decision

Pass 2 establishes the semantic skeleton and prevents the main counting errors:
- file count ≠ experiment count;
- result count ≠ experiment count;
- ID number ≠ experiment count;
- corrected replication ≠ duplicate;
- audit/attack ≠ empirical confirmation;
- CI PASS ≠ scientific validation.

Source of truth remains the original Ω-Lab/ORISIK records; this registry is their normalized connection layer.
