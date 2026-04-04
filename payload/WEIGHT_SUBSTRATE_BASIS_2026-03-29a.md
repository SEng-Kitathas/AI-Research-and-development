# Weight Substrate Basis Document
_Version: 2026-03-29a_

## Purpose
This document supersedes the 2026-03-28a basis after the turn-by-turn read of the early Tesseract MHT thread and the forensic read of the Forge weight-consumption zip.

The project basis is now explicitly:
- a **shared substrate**
- multiple **research branches**
- a standing **shadow documentation layer**
- a living **white paper thesis**
- a tracked **source-thread genealogy**
- a tracked **consumption-pipeline seam**

This is no longer framed as “which one weight format wins?”
It is framed as:
> discover the strongest realizable discrete geometric weight substrate by testing research branches against shared invariants, while treating ingestion/consumption as a first-class bridge rather than an afterthought.

---

## 1. Shared Substrate Invariants (RB-0)

These are non-optional unless explicitly marked experimental.

### SI-1 — Discrete low-bit nativity
Prefer discrete, low-bit, ternary-friendly, or byte-aligned state spaces over unconstrained floating-point weight fields.

### SI-2 — Cheap closed math
Core hot-path transforms should stay within:
- shift
- signed permutation
- add/subtract
- clamp/project
- lookup/reindex

General multiply is not forbidden globally, but it must be justified by branch results rather than assumed by default.

### SI-3 — Structured local objects
The primitive is not a scalar weight. It is a structured local object:
- block
- plane
- grouped tensor/object
- optional 4D lift

### SI-4 — Whole-object and blockwise action
Where possible, the same operator family should act on:
- the whole local object
- its constituent blocks

### SI-5 — Combinatory richness over scalar precision
Expressivity should come primarily from structured composition and legal transforms, not high scalar precision.

### SI-6 — Deterministic auditability
State transitions must be inspectable, replayable, and suitable for exact or near-exact audit.

### SI-7 — Hardware sympathy
The substrate should remain legible to cache behavior, vectorization, integer-friendly execution, compact packing, and locality-aware layout.

### SI-8 — Liftability
Higher-order extensions (spectral layer, 4D geometric space, mutagenic weights) must be lifts of the same local algebra family, not replacements that abandon it.

### SI-9 — Consumption is first-class
Weight ingestion/distillation is not ancillary. The substrate must define how external capability is mapped, filtered, welded, localized, and exported into native form.

---

## 2. Canonical Object Model

### Primitive sets
- `T = {-1, 0, 1}` — ternary base state set
- `B` — block, the smallest structured local carrier
- `P` — plane, an ordered composition of blocks
- `R` — radical, the symbolic/semantic identity assigned to a plane or block composition
- `O` — legal transform/operator family over the substrate
- `C` — consumed external capability unit (organ, motif, block, theorem, weight strip)

### Interpretation
A branch may instantiate these differently, but it must state:
- what a block is
- what a plane is
- how radicals bind
- what the legal transforms are
- what closure means after each transform
- how consumed capability is converted into native substrate form

---

## 3. Research Branch Model

All expression options are treated as **research branches**.
Each branch must define:
1. claim
2. object model
3. operator family
4. packing/encoding
5. update/training rule
6. evaluation tasks
7. evidence status
8. kill criteria

### Branch taxonomy

#### RB-1 — TQ1 / grouped Hamilton branch
Structured grouped algebra using quaternion-style or Hamilton-product-like interactions.

#### RB-2 — TQ2 / plane-block geometric permutation branch
Plane/block substrate using discrete permutation, reindexing, and cheap local transforms.
**Current build-favored branch.**

#### RB-3 — Spectral companion branch
Loop-B style transform family (Fourier/NTT-inspired or exact finite-field spectral layer).

#### RB-4 — 4D mutagenic lift
Higher geometric space for mutation/evolution while preserving cheap local algebra.

#### RB-5 — Native distillation / weight-consumption branch
Consume standard weights/content, distill into substrate-native representation.

#### RB-6 — Control-layer coupling branch
Coupling between weight substrate and holon/nanite/salience-routing control layer.

#### RB-7 — Scheduler/update ablation branch
Schedules, update rules, acceptance criteria, Metropolis/annealing, etc.

---

## 4. Current Normative Position

### Normative today
- the project basis is **branch-based**
- TQ2 is the **current build-favored expression branch**
- TQ1 remains a valid **baseline/an­cestral branch**
- spectral, mutagenic, native-distillation, and control coupling remain live branches
- the Forge/consumption seam is promoted to a **first-class branch family**
- source-thread genealogy is preserved as evidence, not doctrine

### Non-normative until earned
- privileged zeta timing
- blanket end-to-end reversibility claims for the software path
- thermodynamic performance claims on commodity hardware
- “projective inference” as solved rather than hypothesized
- any branch lacking kill criteria or a comparator baseline

---

## 5. Promotion Rules

A branch moves from “interesting” to “real” when it has:
- a defined object model
- a defined operator family
- a reproducible implementation sketch
- at least one task family
- measurable metrics
- explicit failure criteria

A branch moves from “real” to “build-favored” when it:
- survives ablations
- preserves invariants
- improves one or more of:
  - throughput
  - expressivity per byte
  - auditability
  - hardware sympathy
  - training stability
without unacceptable regressions elsewhere.

---

## 6. Evaluation Doctrine

Every branch must be evaluated along the same axes:
- expressivity
- cost
- closure
- auditability
- hardware sympathy
- update/training viability
- degeneracy risk
- branch-specific kill criteria

The consumption branch must additionally be evaluated on:
- ingestion fidelity
- capability retention after conversion
- collision/overwrite behavior
- locality preservation
- export compatibility with the native substrate

---

## 7. Immediate Basis Decisions

1. The MHT thread is a **genealogy source**, not a normative spec.
2. The Forge zip is a **real ingestion architecture** and should be treated as the main evidence seam for RB-5.
3. The current Forge is mature enough to validate the branch, but it is still mostly **pre-TQ2** in scoring/export assumptions.
4. The next rewrite pressure lands on:
   - TQ2 projection-aware scoring
   - motif-aware locality
   - native TQ2/quaternion export
   - rotation-equivalence deduplication
5. Every future session begins by loading:
   - basis doc
   - matrix
   - crosswalk
   - addendum
   - maintenance note
   - white paper
   - source-thread genealogy
