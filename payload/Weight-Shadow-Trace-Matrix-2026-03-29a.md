# Weight Substrate — Shadow Trace Matrix
_Version: 2026-03-29a_

## GOVERNANCE

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| GOV-WS-01 | Shared substrate invariants defined and canonicalized | **Implemented** | T0 | Basis doc 2026-03-29a |
| GOV-WS-02 | Branch model replaces “one true format” framing | **Implemented** | T0 | Canonical |
| GOV-WS-03 | TQ2 is build-favored branch, not sole truth | **Implemented** | T0 | Remains lead branch |
| GOV-WS-04 | Matrix + crosswalk + addendum + maintenance note + white paper are SOP | **Implemented** | T0 | Standing control loop |
| GOV-WS-05 | Source-thread genealogy tracked as evidence layer | **Implemented** | T0 | New support doc |
| GOV-WS-06 | Every branch must define kill criteria | **Partial** | T0 | Still incomplete across branches |

## SHARED SUBSTRATE (RB-0)

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SUB-01 | Discrete low-bit / ternary-friendly nativity | **Implemented** | P0 | Basis invariant |
| SUB-02 | Cheap closed math (shift/permutation/add/clamp/lookup) | **Implemented** | P0 | Basis invariant |
| SUB-03 | Structured local objects (block/plane/group) | **Implemented** | P0 | Basis invariant |
| SUB-04 | Whole-object + blockwise action compatibility | **Partial** | P0 | Needs formal operator definitions |
| SUB-05 | Deterministic auditability | **Implemented** | P0 | Project-level invariant |
| SUB-06 | Hardware sympathy / cache awareness | **Implemented** | P0 | Reinforced by Forge and napkin lineage |
| SUB-07 | Liftability into higher spaces without algebra break | **Partial** | P1 | Needs formalization for RB-4 |
| SUB-08 | Consumption/distillation is first-class | **Implemented** | P0 | Elevated after Forge zip read |

## RB-1 — TQ1 / GROUPED HAMILTON BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB1-01 | Define canonical TQ1 object model | **Partial** | P1 | Ancestral baseline |
| RB1-02 | Define legal operator family | **Partial** | P1 | Hamilton-style grouped interactions |
| RB1-03 | Baseline implementation for comparison | **Missing** | P1 | Needed for fair branch evaluation |
| RB1-04 | Kill criteria | **Missing** | P1 | Must define failure thresholds |

## RB-2 — TQ2 / PLANE-BLOCK GEOMETRIC PERMUTATION BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB2-01 | Canonical plane/block object model | **Partial** | P0 | Napkin + MHT evidence strong |
| RB2-02 | Formal block/plane/radical grammar | **Partial** | P0 | Needs explicit Pattern IR |
| RB2-03 | Cheap operator family (whole vs blockwise) | **Partial** | P0 | Core research seam |
| RB2-04 | Compact encoding and packing | **Partial** | P0 | Build-favored path |
| RB2-05 | Minimal executable skeleton | **Missing** | P0 | Next build target |
| RB2-06 | Kill criteria | **Missing** | P0 | Must be written before deep implementation |

## RB-3 — SPECTRAL COMPANION BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB3-01 | Define spectral object/interaction model | **Partial** | P1 | Loop-B / NTT line |
| RB3-02 | Exact finite-field variant isolated from metaphor | **Partial** | P1 | NTT favored over vague Fourier language |
| RB3-03 | Comparator vs no-spectral baseline | **Missing** | P1 | Required |
| RB3-04 | Kill criteria | **Missing** | P1 | Required |

## RB-4 — 4D MUTAGENIC LIFT

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB4-01 | Formal 4D lift preserving local cheap algebra | **Partial** | P1 | User clarified this explicitly |
| RB4-02 | Cache/packing model | **Partial** | P1 | Byte-aligned options discussed; not settled |
| RB4-03 | Mutation/update semantics | **Missing** | P1 | Open |
| RB4-04 | Kill criteria | **Missing** | P1 | Open |

## RB-5 — NATIVE DISTILLATION / WEIGHT CONSUMPTION

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB5-01 | Consumption branch promoted to first-class status | **Implemented** | P0 | After Forge zip read |
| RB5-02 | Forge pipeline: Surgeon / Scientist / Engineer / Artificer | **Implemented** | P0 | Real Rust code exists |
| RB5-03 | Meritocratic overwrite rule (>2% threshold) | **Implemented** | P0 | Current Artificer logic |
| RB5-04 | 7-stage source-agnostic pipeline documented | **Implemented** | P0 | Download → Validate → Calibrate → Locality → CRHQ → Ghost → Radical Export |
| RB5-05 | TQ2 projection-aware scoring | **Missing** | P0 | Current Scientist is still entropy/source/position/type heavy |
| RB5-06 | Motif-aware locality replacing pure hash locality | **Missing** | P1 | Current Engineer is radical + hash sequence |
| RB5-07 | Native TQ2/quaternion export path | **Missing** | P0 | Current export seals raw blobs/radicals, not TQ2-native weights |
| RB5-08 | Rotation-equivalence / symmetry deduplication | **Missing** | P1 | Proposed in thread, not in code |
| RB5-09 | Forge-to-CIL provenance and persistent memory bridge | **Partial** | P1 | Present in docs, not validated here |
| RB5-10 | Kill criteria | **Missing** | P0 | Must define fidelity/cost failure conditions |

## RB-6 — CONTROL-LAYER COUPLING

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB6-01 | Control lineage preserved (salience/sparsity/stigmergy/heartbeat) | **Implemented** | P1 | Genealogy doc |
| RB6-02 | Explicit coupling model to weight substrate | **Partial** | P1 | Still conceptual |
| RB6-03 | Organ formation thresholds | **Missing** | P2 | Open seam inherited from KarnOS |
| RB6-04 | Kill criteria | **Missing** | P2 | Needed |

## RB-7 — SCHEDULER / UPDATE ABLATIONS

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB7-01 | Update-rule comparison suite | **Missing** | P1 | Threshold vs Metropolis vs others |
| RB7-02 | Schedule comparison suite | **Missing** | P1 | Fixed periodic vs branch experiments |
| RB7-03 | Zeta scheduling demoted to experiment condition | **Implemented** | P1 | No longer normative |
| RB7-04 | Kill criteria | **Missing** | P1 | Required |

## SOURCE-THREAD GENEALOGY

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| GENE-01 | Early MHT thread folded into evidence chain | **Implemented** | P0 | New genealogy doc |
| GENE-02 | Thread claims split into grounded vs speculative | **Partial** | P0 | Needs continued curation |
| GENE-03 | Napkin artifacts preserved as ancestral evidence | **Implemented** | P0 | Already promoted |

## OPEN DECISIONS

| OD | Question | Status | Priority |
|---|---|---|---|
| WS-01 | What is the canonical RB-2 object grammar? | Open | P0 |
| WS-02 | What are branch kill criteria across RB-1..RB-7? | Open | P0 |
| WS-03 | Should RB-5 score by geometric resonance rather than entropy-first heuristics? | Open | P0 |
| WS-04 | Should Engineer locality remain hash-driven or become motif-aware? | Open | P1 |
| WS-05 | What is the canonical native export format into TQ2/quaternion substrate? | Open | P0 |
| WS-06 | What is the smallest faithful RB-2 executable skeleton? | Open | P0 |
