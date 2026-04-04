# Weight Substrate — Shadow Trace Matrix
_Version: 2026-03-28a_

## GOVERNANCE

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| GOV-WS-01 | Shared substrate invariants defined and canonicalized | **Implemented** | T0 | See basis doc RB-0 |
| GOV-WS-02 | Branch model replaces “one true format” framing | **Implemented** | T0 | All major expression options are research branches |
| GOV-WS-03 | TQ2 is current build-favored branch, not sole truth | **Implemented** | T0 | TQ2 remains lead branch |
| GOV-WS-04 | Matrix + crosswalk + addendum + maintenance note + white paper are SOP | **Implemented** | T0 | Standing control loop until project resolution |
| GOV-WS-05 | Every branch must define kill criteria | **Partial** | T0 | Some branches still missing explicit kill criteria |

## SHARED SUBSTRATE (RB-0)

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SUB-01 | Discrete low-bit / ternary-friendly nativity | **Implemented** | P0 | Basis invariant |
| SUB-02 | Cheap closed math (shift/permutation/add/clamp/lookup) | **Implemented** | P0 | Basis invariant |
| SUB-03 | Structured local objects (block/plane/group) | **Implemented** | P0 | Basis invariant |
| SUB-04 | Whole-object + blockwise action compatibility | **Partial** | P0 | Requires formal operator definitions |
| SUB-05 | Deterministic auditability | **Implemented** | P0 | Project-level invariant |
| SUB-06 | Hardware sympathy / cache awareness | **Implemented** | P0 | Reinforced by native-distillation lineage |
| SUB-07 | Liftability into higher spaces without algebra break | **Partial** | P1 | Needs formalization for RB-4 |

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
| RB2-01 | Canonical plane/block object model | **Partial** | P0 | Napkin evidence now strong |
| RB2-02 | Formal block/plane/radical grammar | **Partial** | P0 | Needs explicit IR |
| RB2-03 | Cheap operator family (whole vs blockwise) | **Partial** | P0 | Core research seam |
| RB2-04 | Compact encoding and packing | **Partial** | P0 | Build-favored path |
| RB2-05 | Minimal executable skeleton | **Missing** | P0 | Next build target |
| RB2-06 | Kill criteria | **Missing** | P0 | Must be written before deep implementation |

## RB-3 — SPECTRAL COMPANION BRANCH

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB3-01 | Define spectral layer as lift, not replacement | **Partial** | P1 | Fourier/NTT ancestry |
| RB3-02 | Exact transform candidate (NTT) | **Partial** | P1 | Research-backed seam |
| RB3-03 | Coupling rules with RB-2 | **Missing** | P1 | Needs formal integration |
| RB3-04 | Kill criteria | **Missing** | P1 | TBD |

## RB-4 — 4D MUTAGENIC LIFT

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB4-01 | Define 4D object model as lift of base algebra | **Partial** | P1 | “Mutagenic weights” branch |
| RB4-02 | Preserve cheap-math closure in 4D | **Missing** | P1 | Core feasibility gate |
| RB4-03 | Mutation/update semantics | **Missing** | P1 | TBD |
| RB4-04 | Kill criteria | **Missing** | P1 | TBD |

## RB-5 — NATIVE DISTILLATION / WEIGHT CONSUMPTION

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB5-01 | Formalize “consume standard weights / distill content” | **Partial** | P1 | Strong ancestral lineage |
| RB5-02 | Teacher-student substrate distillation path | **Partial** | P1 | Supported by literature directionally |
| RB5-03 | Native packing target | **Missing** | P1 | Need exact target representation |
| RB5-04 | Kill criteria | **Missing** | P1 | TBD |

## RB-6 — CONTROL-LAYER COUPLING

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB6-01 | Holon ↔ Nanite isomorphism preserved | **Partial** | P1 | Strong ancestral signal |
| RB6-02 | Salience/sparsity/heartbeat coupling | **Partial** | P1 | Control lineage |
| RB6-03 | Weight substrate ↔ routing interface | **Missing** | P1 | Needs interface contract |
| RB6-04 | Kill criteria | **Missing** | P1 | TBD |

## RB-7 — SCHEDULER / UPDATE ABLATIONS

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| RB7-01 | Metropolis / annealing branch | **Partial** | P1 | Research-backed enough to test |
| RB7-02 | Fixed periodic scheduler baseline | **Missing** | P0 | Mandatory baseline |
| RB7-03 | Prime/zeta scheduler ablation | **Missing** | P2 | Experimental only |
| RB7-04 | Strong reversibility claims removed from normative layer | **Implemented** | P0 | Now speculative-only |
| RB7-05 | Kill criteria per schedule/update branch | **Missing** | P1 | TBD |

## WHITE PAPER / DOCUMENTATION

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| DOC-01 | White paper rewritten around substrate+branches | **Implemented** | P0 | v0.1 created |
| DOC-02 | Research crosswalk updated with napkin genealogy | **Implemented** | P0 | 2026-03-28a |
| DOC-03 | Addendum captures branch-basis decision | **Implemented** | P0 | 2026-03-28a |
| DOC-04 | Session SOP explicitly includes all control docs | **Implemented** | P0 | Maintenance note |
| DOC-05 | Basis doc referenced first in future sessions | **Implemented** | P0 | New rule |

## IMMEDIATE NEXT BUILD PRESSURE

1. Write RB-2 object model and operator grammar.
2. Write kill criteria for RB-1 through RB-7.
3. Implement minimal RB-2 executable skeleton.
4. Preserve RB-1 as baseline comparator.
5. Add baseline scheduler/update rows before new branch growth.
