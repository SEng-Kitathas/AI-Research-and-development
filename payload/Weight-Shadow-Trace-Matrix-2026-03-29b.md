# Weight Substrate — Shadow Trace Matrix
_Version: 2026-03-29b_

## GOVERNANCE

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| GOV-WS-01 | Shared substrate invariants defined and canonicalized | **Implemented** | T0 | Basis doc |
| GOV-WS-02 | Branch model replaces “one true format” framing | **Implemented** | T0 | Canonical |
| GOV-WS-03 | TQ2 is build-favored branch, not sole truth | **Implemented** | T0 | Remains lead branch |
| GOV-WS-04 | Matrix + crosswalk + addendum + maintenance note + white paper are SOP | **Implemented** | T0 | Standing control loop |
| GOV-WS-05 | Source-thread genealogy tracked as evidence layer | **Implemented** | T0 | Maintained |
| GOV-WS-06 | Every branch must define kill criteria | **Partial** | T0 | Grammar/harness now define RB-2 structure |

## SHARED SUBSTRATE (RB-0)

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SUB-01 | Discrete low-bit / ternary-friendly nativity | **Implemented** | P0 | Basis invariant |
| SUB-02 | Cheap closed math (shift/permutation/add/clamp/lookup) | **Implemented** | P0 | Basis invariant |
| SUB-03 | Structured local objects (block/plane/group) | **Implemented** | P0 | Basis invariant |
| SUB-04 | Whole-object + blockwise action compatibility | **Implemented** | P0 | Now formalized in object grammar |
| SUB-05 | Deterministic auditability | **Implemented** | P0 | Project-level invariant |
| SUB-06 | Hardware sympathy / cache awareness | **Implemented** | P0 | Basis invariant |
| SUB-07 | Liftability into higher spaces without algebra break | **Partial** | P1 | RB-4 still open |
| SUB-08 | Consumption/distillation is first-class | **Implemented** | P0 | Basis invariant |
| SUB-09 | Instrumented benchmark harness exists | **Implemented** | P0 | Harness spec added |

## RB-1 — TQ1 / GROUPED HAMILTON BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB1-01 | Define canonical TQ1 object model | **Partial** | P1 | Ancestral baseline |
| RB1-02 | Define legal operator family | **Partial** | P1 | Hamilton-style grouped interactions |
| RB1-03 | Baseline implementation for comparison | **Missing** | P1 | Needed |
| RB1-04 | Kill criteria | **Missing** | P1 | Must define |

## RB-2 — TQ2 / PLANE-BLOCK GEOMETRIC PERMUTATION BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB2-01 | Canonical plane/block object model | **Implemented** | P0 | TQ2 Object Grammar |
| RB2-02 | Formal block/plane/radical grammar | **Implemented** | P0 | TQ2 Object Grammar |
| RB2-03 | Cheap operator family (whole vs blockwise) | **Implemented** | P0 | Formalized for RB-2A/B/C |
| RB2-04 | Compact encoding and packing | **Partial** | P0 | Physical packing still implementation-specific |
| RB2-05 | Minimal executable skeleton | **Partial** | P0 | Toy probe exists; real skeleton still needed |
| RB2-06 | Kill criteria | **Implemented** | P0 | Defined in grammar/harness |
| RB2-07 | Benchmark harness tasks and metrics | **Implemented** | P0 | Harness spec added |
| RB2-08 | RB-2C hybrid branch formalized | **Implemented** | P0 | Likely practical winner candidate |

## RB-3 — SPECTRAL COMPANION BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB3-01 | Define spectral object/interaction model | **Partial** | P1 | Loop-B / NTT line |
| RB3-02 | Exact finite-field variant isolated from metaphor | **Partial** | P1 | NTT favored |
| RB3-03 | Comparator vs no-spectral baseline | **Missing** | P1 | Required |
| RB3-04 | Kill criteria | **Missing** | P1 | Required |

## RB-4 — 4D MUTAGENIC LIFT

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB4-01 | Formal 4D lift preserving local cheap algebra | **Partial** | P1 | Open seam |
| RB4-02 | Cache/packing model | **Partial** | P1 | Open seam |
| RB4-03 | Mutation/update semantics | **Missing** | P1 | Open |
| RB4-04 | Kill criteria | **Missing** | P1 | Open |

## RB-5 — NATIVE DISTILLATION / WEIGHT CONSUMPTION

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB5-01 | Consumption branch promoted to first-class status | **Implemented** | P0 | Canonical |
| RB5-02 | Forge pipeline: Surgeon / Scientist / Engineer / Artificer | **Implemented** | P0 | Real code exists |
| RB5-03 | Meritocratic overwrite rule (>2% threshold) | **Implemented** | P0 | Current Forge |
| RB5-04 | 7-stage source-agnostic pipeline documented | **Implemented** | P0 | Current Forge |
| RB5-05 | TQ2 projection-aware scoring | **Missing** | P0 | Rewrite pressure |
| RB5-06 | Motif-aware locality replacing pure hash locality | **Missing** | P1 | Rewrite pressure |
| RB5-07 | Native TQ2/quaternion export path | **Missing** | P0 | Rewrite pressure |
| RB5-08 | Rotation-equivalence / symmetry deduplication | **Missing** | P1 | Rewrite pressure |
| RB5-09 | Forge-to-CIL provenance and persistent memory bridge | **Partial** | P1 | Still open |
| RB5-10 | Kill criteria | **Missing** | P0 | Must define fidelity/cost failure conditions |

## RB-6 — CONTROL-LAYER COUPLING

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB6-01 | Control lineage preserved (salience/sparsity/stigmergy/heartbeat) | **Implemented** | P1 | Genealogy maintained |
| RB6-02 | Explicit coupling model to weight substrate | **Partial** | P1 | Still conceptual |
| RB6-03 | Organ formation thresholds | **Missing** | P2 | Open seam |
| RB6-04 | Kill criteria | **Missing** | P2 | Needed |

## RB-7 — SCHEDULER / UPDATE ABLATIONS

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB7-01 | Update-rule comparison suite | **Missing** | P1 | Threshold vs Metropolis vs others |
| RB7-02 | Schedule comparison suite | **Missing** | P1 | Fixed periodic vs branch experiments |
| RB7-03 | Zeta scheduling demoted to experiment condition | **Implemented** | P1 | Non-normative |
| RB7-04 | Kill criteria | **Missing** | P1 | Required |

## LAB INSTRUMENTATION

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| LAB-01 | TQ2 object grammar exists | **Implemented** | P0 | New canonical doc |
| LAB-02 | Benchmark harness spec exists | **Implemented** | P0 | New canonical doc |
| LAB-03 | Shared seed/split/metric protocol | **Implemented** | P0 | Harness spec |
| LAB-04 | Failure mode tracking is mandatory | **Implemented** | P0 | Harness spec |
| LAB-05 | Branch home-task rule enforced | **Implemented** | P0 | Branch must win where it claims advantage |

## OPEN DECISIONS

| OD | Question | Status | Priority |
|---|---|---|---|
| WS-01 | What is the smallest faithful RB-2 executable skeleton? | Open | P0 |
| WS-02 | What are branch kill criteria across RB-1..RB-7 beyond RB-2? | Open | P0 |
| WS-03 | Should RB-5 score by geometric resonance rather than entropy-first heuristics? | Open | P0 |
| WS-04 | Should Engineer locality remain hash-driven or become motif-aware? | Open | P1 |
| WS-05 | What is the canonical native export format into TQ2/quaternion substrate? | Open | P0 |
| WS-06 | Does RB-2C hybrid actually outperform RB-2A and RB-2B on mixed tasks? | Open | P0 |
