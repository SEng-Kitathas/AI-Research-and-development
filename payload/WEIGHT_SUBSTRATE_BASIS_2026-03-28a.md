# Weight Substrate Basis Document
_Version: 2026-03-28a_

## Purpose
This document establishes the basis for the weight-substrate project after the forensic read, crosswalk pass, and napkin extraction pass.

This is now the project basis:
- a **shared substrate**
- multiple **research branches**
- a standing **shadow documentation layer**
- a living **white paper thesis**

The project is no longer framed as “find the one true weight format.”
It is framed as:
> discover the strongest realizable discrete geometric weight substrate by testing research branches against shared invariants.

---

## 1. Shared Substrate Invariants (RB-0)

These are the non-optional constraints that all branches must satisfy unless explicitly marked experimental.

### SI-1 — Discrete low-bit nativity
The substrate must prefer discrete, low-bit, or ternary-friendly state spaces over unconstrained floating-point weight fields.

### SI-2 — Cheap closed math
Core transforms should be expressible through cheap operations:
- shift
- signed permutation
- add/subtract
- clamp/project
- lookup/reindex

General multiply should not be required on the hot path unless a branch explicitly earns that cost.

### SI-3 — Structured local objects
The primitive is not “a scalar weight.”
The primitive is a structured local object:
- block
- plane
- grouped tensor/object
- optional 4D lift

### SI-4 — Whole-object and blockwise action
The same operator family should, where possible, act on both:
- the whole local object
- its constituent blocks

### SI-5 — Combinatory richness over scalar precision
Expressivity should come primarily from structured composition and legal transforms, not from high scalar precision.

### SI-6 — Deterministic auditability
State transitions must be inspectable, replayable, and suitable for exact or near-exact audit.

### SI-7 — Hardware sympathy
The substrate should remain legible to cache behavior, vectorization, integer-friendly execution, and compact packing.

### SI-8 — Liftability
Higher-order extensions (spectral layer, 4D geometric space, mutagenic weights) should be lifts of the same local algebra, not replacements that abandon it.

---

## 2. Canonical Object Model

### Primitive sets
- `T = {-1, 0, 1}` — ternary base state set
- `B` — block, the smallest structured local carrier
- `P` — plane, an ordered composition of blocks
- `R` — radical, the symbolic/semantic identity assigned to a plane or block composition
- `O` — legal transform/operator family over the substrate

### Interpretation
A branch may instantiate these differently, but it must say what:
- a block is
- a plane is
- how radicals bind
- what the legal transforms are
- what closure means after each transform

---

## 3. Research Branch Model

All expression options are now treated as **research branches**.

A branch is not a sketch or a preference.
A branch must define:
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
- The project basis is **branch-based**
- TQ2 is the **current build-favored expression branch**
- TQ1 remains a valid **baseline/an­cestral branch**
- spectral, mutagenic, and native-distillation ideas remain live branches
- zeta-scheduler and strong software reversibility claims are **not normative**

### Non-normative until earned
- privileged zeta timing
- blanket end-to-end reversibility claims for the software path
- thermodynamic performance claims on commodity hardware
- any branch that cannot state its kill criteria

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

### E-1 — Expressivity
Can it represent useful local and global structure?

### E-2 — Cost
How many bits, bytes, ops, and memory movements does it require?

### E-3 — Closure
Does it remain in-family under its legal transforms?

### E-4 — Auditability
Can the state transitions be replayed and inspected?

### E-5 — Hardware sympathy
Does it map cleanly to integer/vector/cache-friendly execution?

### E-6 — Training/update viability
Can it be updated without abandoning the substrate’s cheap-math constraints?

### E-7 — Degeneracy risk
Does the combinatory space yield useful distinctions, or mostly aliases/redundancies?

---

## 7. Research-Grounded Seams

The following seams are supported directionally by external research:

- ternary / low-bit discrete inference and hardware-friendly packing
- integer-only or low-bit training/inference
- quaternion/hypercomplex grouped representations
- exact/integer spectral transforms (e.g. NTT)
- knowledge distillation into smaller/native representations
- sparse/addition-friendly ternary arithmetic

The following remain speculative or weakly grounded:
- zeta scheduling as a privileged update law
- strong software-path reversibility claims
- p-adic archive advantages in the current project stage

---

## 8. Immediate Basis Decisions

1. The white paper thesis must be rewritten around **substrate invariants + research branches**.
2. The matrix must track branches as first-class rows.
3. Napkin artifacts count as ancestral design evidence and belong in the crosswalk/addendum.
4. Every session begins by loading:
   - basis doc
   - matrix
   - crosswalk
   - addendum
   - maintenance note
   - white paper
5. The next implementation effort should target the smallest buildable RB-2 skeleton while preserving RB-1 as a baseline.

---

## 9. Basis Sentence

> Richness comes from structured discrete composition under cheap closed operators, not from scalar precision.

That sentence is now the core statement of the branch program.
