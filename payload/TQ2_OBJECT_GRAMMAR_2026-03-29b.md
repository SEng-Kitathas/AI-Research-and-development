# TQ2 Object Grammar
_Version: 2026-03-29b_

## Purpose
This document formalizes the current build-favored substrate branch (RB-2) into a lab-grade object grammar.
It is intentionally boring. It exists so the substrate can be implemented, benchmarked, audited, and killed if necessary.

---

## 1. Scope
This grammar defines:
- the canonical RB-2 object model
- legal transforms
- closure rules
- scoring surfaces
- branch variants (whole-plane, blockwise, hybrid)
- invariants any implementation must preserve

This document does **not** assume:
- quaternion lift is canonical
- spectral Loop B is canonical
- Forge export is solved
- projective inference is solved

Those remain separate research branches.

---

## 2. Primitive Sets

### 2.1 Ternary base set
`T = {-1, 0, 1}`

Interpretation:
- `-1` = antagonistic / negative phase / inverse pole
- `0` = null / neutral / inactive
- `1` = excitatory / positive phase / forward pole

These meanings are branch-local conveniences, not universal metaphysics.
The only canonical truth is membership in `T`.

### 2.2 Indices
- `i` = block-local cell index
- `b` = block index within a plane
- `p` = plane index
- `r` = radical identifier
- `k` = transform identifier

---

## 3. Core Objects

### 3.1 Cell
A cell is a single ternary state:
`c ∈ T`

### 3.2 Block
A block is the smallest structured local carrier.
Canonical default for RB-2b:
`B = [c1, c2, c3]` where each `ci ∈ T`

This default treats a block as a 1×3 ordered ternary strip.
Alternative block shapes may be explored later, but any branch that changes block shape must state so explicitly.

### 3.3 Plane
A plane is an ordered composition of blocks.
Canonical default:
`P = [B1, B2, B3]`

Expanded, the canonical plane is a 3×3 ternary object containing 9 ternary cells.

### 3.4 Radical
A radical is a symbolic/semantic binding attached to a plane or plane family.
A radical is represented as:
- `r.id`
- `r.prototype`
- `r.metadata`

Minimum required fields:
- stable identifier
- canonical prototype plane
- transform family allowed for matching

### 3.5 Plane Family
A plane family is a set of equivalent planes under a legal transform family.
`F(r) = { O_k(P_r) }`

This is the key RB-2 move:
classification is often done against a **family** rather than a single raw plane.

---

## 4. Canonical Branch Variants

### 4.1 RB-2A — Whole-plane transform branch
Treat the plane as one object.
Legal transforms act on all 9 cells together.

Best used when invariants are global, geometric, or motif-level.

### 4.2 RB-2B — Blockwise transform branch
Treat each block as a local object.
Legal transforms act block-by-block.
Whole-plane score is aggregated from block-level scores.

Best used when invariants are compositional or local.

### 4.3 RB-2C — Hybrid branch
Use blockwise scoring as the local substrate and whole-plane transforms as alignment/correction.

This is currently the most likely practical winner, but it is **not** assumed solved.

---

## 5. Legal Transform Families

All RB-2 transforms must remain inside cheap closed math.

### 5.1 Whole-plane transforms
Allowed default set:
- identity
- 90° rotation
- 180° rotation
- 270° rotation
- horizontal reflection
- vertical reflection
- optional diagonal reflections

Implementation target:
- index remap
- signed permutation
- lookup

Forbidden as default hot-path assumptions:
- generic floating-point matrix multiply
- non-closed unconstrained rescaling

### 5.2 Blockwise transforms
Allowed default set:
- identity
- left cyclic shift
- right cyclic shift
- optional signed inversion

Implementation target:
- rotate register positions
- shift/reindex
- sign flip if explicitly enabled

### 5.3 Hybrid transforms
A hybrid implementation may perform:
1. local block transforms
2. block aggregation
3. one whole-plane correction or alignment step

Hybrid branches must report each stage separately.

---

## 6. Closure Rules

### 6.1 State closure
Every transform must return a valid object over `T`.
No transform may emit out-of-domain values without an explicit projection step.

### 6.2 Structural closure
A legal transform must preserve object type:
- block → block
- plane → plane
- plane family member → plane family member candidate

### 6.3 Audit closure
Every transform must be replayable as:
- input object
- transform id
- output object

### 6.4 Aggregation closure
If a score is aggregated from blocks, the aggregator must be deterministic and bounded.

Canonical default aggregators:
- sum of best local alignments
- weighted sum with fixed compile-time weights
- max-plus style winner aggregation

---

## 7. Scoring Surfaces

### 7.1 Whole-plane score
`S_whole(P, r) = max_k sim(P, O_k(P_r))`

Where `sim` is a bounded similarity function.
Canonical default:
- cell agreement count
- signed agreement score
- Hamming-style agreement with ternary awareness

### 7.2 Blockwise score
`S_block(P, r) = Σ_b max_k sim(B_b, O_k(B_r,b))`

### 7.3 Hybrid score
`S_hybrid = α·S_block + β·S_whole + γ·S_cross`

Where:
- `S_cross` is an optional cross-block coherence term
- `α, β, γ` must be fixed and reported

No hidden adaptive weights in the benchmark harness.

---

## 8. Packing and Encoding

### 8.1 Canonical logical representation
The canonical logical plane is 9 ternary cells.

### 8.2 Physical representation
Physical packing is implementation-specific but must document:
- bits per cell
- bits per block
- bits per plane
- byte alignment strategy
- vectorization strategy

### 8.3 Current build preference
Prefer byte- and cache-legible layouts over density tricks that complicate transforms.

That means:
- nibble-level packing is allowed
- but byte-aligned intermediate representations are acceptable if they improve transform simplicity and auditability

---

## 9. Radical Binding Rules

### 9.1 Prototype binding
Every radical must own one canonical prototype plane.

### 9.2 Family binding
A radical may also define its legal family under transforms.

### 9.3 Semantic binding
Metadata may include:
- task family
- source lineage
- consumption provenance
- confidence band

### 9.4 No free-floating symbolism
A radical without a prototype or family is not valid for benchmarking.

---

## 10. Implementation Levels

### 10.1 Level 0 — Spec object
Pure Python/Rust/ASM-agnostic object model.

### 10.2 Level 1 — Reference object
Clear, slow, obviously correct implementation.

### 10.3 Level 2 — Hot-path object
Packed, vectorizable, cache-aware implementation.

Every optimization must be provably equivalent to Level 1 on the same transform set.

---

## 11. Kill Criteria for RB-2 Variants

### RB-2A whole-plane kill criteria
Kill or demote if:
- it fails to beat baseline on global-geometric tasks
- it underperforms hybrid on both global and mixed tasks
- transform cost outweighs accuracy gain materially

### RB-2B blockwise kill criteria
Kill or demote if:
- it fails to beat or match baseline on local/compositional tasks
- it cannot preserve useful local invariants under cheap transforms
- aggregation produces unstable class aliases

### RB-2C hybrid kill criteria
Kill or demote if:
- added complexity gives no cross-task advantage
- whole-plane correction never contributes meaningfully
- it collapses into either RB-2A or RB-2B in practice

---

## 12. Immediate Deliverables

1. Reference implementation for RB-2A
2. Reference implementation for RB-2B
3. Reference implementation for RB-2C
4. Shared transform test suite
5. Shared closure test suite
6. Shared benchmark harness

---

## 13. Canonical Summary

RB-2 is now formally defined as:

> a 3×3 ternary plane substrate composed of ordered ternary blocks, evaluated under cheap deterministic transforms, with radicals bound to prototype planes or plane families, and with whole-plane, blockwise, and hybrid scoring treated as sibling expression branches.
