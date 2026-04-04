# TQ2 Benchmark Harness Specification
_Version: 2026-03-29b_

## Purpose
This harness exists to turn the TQ2 substrate from a conversation into an instrument.

Its job is to compare RB-2 variants and adjacent branches under shared conditions.
It is not designed to flatter the architecture.
It is designed to kill weak branches quickly.

---

## 1. Branches Under Test

Minimum required comparators:
- `BASE-0` — plain ternary baseline
- `RB-2A` — whole-plane transforms
- `RB-2B` — blockwise transforms
- `RB-2C` — hybrid transforms

Optional later comparators:
- `RB-1` grouped/Hamilton baseline
- `RB-3` spectral companion branch
- `RB-4` 4D mutagenic lift
- `RB-5` consumed/projection-native planes from Forge

---

## 2. Evaluation Rules

### 2.1 Shared-data rule
All branches must see the same datasets, splits, and seeds.

### 2.2 Shared-metric rule
All branches must report the same core metrics.

### 2.3 Reference-first rule
Every optimized implementation must be checked against a slow reference implementation.

### 2.4 No hidden adaptivity rule
Branch-specific heuristics are allowed only if declared.
Undeclared adaptive behavior invalidates the result.

---

## 3. Task Families

### T1 — Whole-plane motif invariance
Label depends on global plane geometry under rotation/reflection.
Purpose: tests RB-2A upside.

### T2 — Block composition invariance
Label depends on local block composition under block-local transforms.
Purpose: tests RB-2B upside.

### T3 — Majority-sign / polarity sanity
Simple task where cheap baselines should remain competitive.
Purpose: detects branch vanity and unnecessary complexity.

### T4 — Mixed global+local motifs
Label depends on both local blocks and global arrangement.
Purpose: primary test bed for RB-2C hybrid viability.

### T5 — Tiny symbolic sequence task
Short sequence continuation or state-tracking task over ternary or small alphabets.
Purpose: tests whether the substrate survives contact with temporal structure.

### T6 — Tiny associative recall
Map compressed cues to stored radicals/planes.
Purpose: tests retrieval shape and aliasing behavior.

### T7 — Tiny teacher-distillation transfer
Use a tiny external teacher to generate labels or logits, then evaluate whether the branch can preserve useful behavior.
Purpose: first bridge to RB-5.

---

## 4. Datasets

### 4.1 Synthetic datasets
Required for T1–T4.
Must be procedurally generated and reproducible by seed.

### 4.2 Sequence datasets
Required for T5.
Should begin with tiny artificial grammars before natural language.

### 4.3 Distillation datasets
Required for T7.
Start with deliberately tiny teacher models and narrow task families.

---

## 5. Core Metrics

Every run must emit:
- accuracy
- macro-F1 where relevant
- stability across seeds
- operations per inference
- transform count per inference
- bytes touched per inference
- storage footprint
- error family notes

Optional but encouraged:
- cache-miss proxy
- vectorization utilization proxy
- exact replay hash

---

## 6. Branch-Specific Metrics

### RB-2A
- global motif retention
- transform-family alias rate
- geometric invariance gain over baseline

### RB-2B
- local motif retention
- block alias rate
- aggregation instability rate

### RB-2C
- hybrid gain over best single branch
- whole-plane correction contribution
- complexity tax per added accuracy point

### RB-5 later
- teacher behavior retention
- projection loss
- conversion cost
- provenance retention

---

## 7. Failure Modes to Track

- branch near chance on its supposed home task
- branch only wins on tasks it implicitly defines
- branch advantage disappears across seeds
- branch creates excessive aliases/collisions
- branch gains accuracy only by exploding transform count
- branch loses auditability when optimized

These are not edge notes. They are first-class outputs.

---

## 8. Experimental Protocol

### 8.1 Minimum run protocol
For each task family:
- at least 20 random seeds for synthetic tasks
- fixed train/validation/test split policy
- report mean and standard deviation

### 8.2 Equivalence protocol
Before benchmarking an optimized branch:
- compare every transform output against reference branch implementation
- compare replay traces on a fixed seed bank

### 8.3 Promotion protocol
A branch may be promoted only if it:
- beats the baseline on the task family it claims to target
- remains stable across seeds
- does not impose unacceptable cost for the gain

---

## 9. Reference Implementation Requirements

The harness repository or module must contain:
- canonical object constructors
- transform library
- similarity functions
- dataset generators
- evaluator
- result serializer
- replay checker

Outputs required:
- CSV metrics
- markdown summary
- branch comparison table
- failure notes

---

## 10. First Wave Plan

### Wave 1 — already partially done
- T1 whole-plane invariant motif
- T2 block composition invariant
- T3 majority-sign sanity

### Wave 2 — immediate next
- T4 mixed global+local motifs
- T5 tiny symbolic sequence
- RB-2C hybrid branch

### Wave 3 — bridge to consumption
- T7 tiny teacher-distillation transfer
- first RB-5 to RB-2 export test

---

## 11. Kill Criteria

A branch should be killed or demoted when:
- it cannot win on its home task family
- it offers no cross-task benefit
- it imposes complexity without measurable gain
- it breaks auditability under optimization
- a simpler branch subsumes it

---

## 12. Canonical Output Statement

The benchmark harness exists to answer one question:

> which TQ2 expression branch delivers the best tradeoff between expressive structure, cheap closure, auditability, and hardware sympathy on shared tasks?
