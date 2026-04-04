# TQ2 Integrated Inference Architecture
_Version: 2026-03-29c_

## Core Decision

**Whole-plane, blockwise, and hybrid are no longer treated as mutually exclusive runtime alternatives.**
They remain separate **research branches for benchmarking**, but the canonical runtime model now treats them as **cooperating inference strata** within one TQ2 substrate.

This means:

- **Research mode** isolates them to measure contribution.
- **Runtime mode** composes them into one inference pipeline.

## Why this shift is warranted

The substrate probe showed that:

- whole-plane transforms win when the task invariant is genuinely global/geometric
- blockwise transforms win or remain competitive when the task invariant is local/compositional
- plain baselines still matter on trivial/global-sign tasks

The correct conclusion is not “pick one.”
It is:

> global invariants and local invariants both exist in real problems, so the substrate should carry both.

## Canonical Runtime Stack

### Layer 0 — Primitive state
- Primitive domain: `T = {-1, 0, 1}`
- Primitive object: `Block`
- Composite object: `Plane`
- Optional lift: `PlaneStack` / `MultiPlane` / future quaternion lift

### Layer 1 — Blockwise local pass
Purpose:
- extract local compositional signal
- reward motif reuse at small scale
- provide cheap local evidence

Operations:
- cyclic block shift
- signed permutation
- add/subtract
- clamp/projection back into `T`

Output:
- per-block alignment score
- per-block transform ID
- local confidence

### Layer 2 — Whole-plane global pass
Purpose:
- detect geometry that only appears at full-plane scale
- enforce global coherence
- catch symmetries invisible to block-local analysis

Operations:
- whole-plane rotations
- reflections
- full-plane signed permutation
- cheap aggregate scoring

Output:
- plane-level alignment score
- plane transform ID
- global confidence

### Layer 3 — Hybrid reconciliation
Purpose:
- fuse local and global evidence
- resolve disagreement
- decide whether the object is best interpreted as:
  - primarily local/compositional
  - primarily global/geometric
  - mixed

Mechanism:
- weighted score fusion
- confidence-aware arbitration
- optional veto logic
- optional contradiction penalty

Output:
- final plane score
- final transform path
- explanatory decomposition

## Canonical Inference Policy

A single input object should pass through:

1. blockwise local scoring
2. whole-plane global scoring
3. hybrid reconciliation
4. final selection / projection

This yields one runtime path, not three separate programs.

## Runtime interpretation

### Local-first interpretation
When blockwise confidence is high and whole-plane confidence is low:
- favor compositional explanation
- preserve block identities
- use whole-plane only as a weak prior

### Global-first interpretation
When whole-plane confidence is high and blockwise confidence is fragmented:
- favor global symmetry explanation
- treat blocks as support structure
- let plane transform dominate

### Mixed interpretation
When both are strong:
- use hybrid composition
- record both local evidence and global transform
- treat this as the ideal case for the substrate

## Why hybrid is still separate in research

Even though runtime composes them, research must still isolate them because:

- otherwise you cannot tell where performance comes from
- otherwise whole-plane glamour can hide blockwise necessity
- otherwise blockwise utility can flatten genuine geometric gains

So the rule is:

- **separate in benchmarking**
- **composed in runtime**

## Canonical operator family

All strata must remain inside the cheap closed operator family:

- shift
- permutation
- sign flip
- add/subtract
- clamp/projection
- lookup/table-driven transform

No branch is allowed to smuggle in heavy generic arithmetic and still claim substrate purity.

## Immediate consequences

1. The canonical engine is now a **stacked TQ2 inference architecture**
2. RB-2A / RB-2B / RB-2C remain valid as **benchmark isolates**
3. The benchmark harness must report both:
   - isolated branch performance
   - integrated runtime performance
4. Forge translation must eventually target both:
   - local motif compatibility
   - global geometric compatibility

## Updated doctrine

> The substrate is one thing.
> The branches are how we measure it.
> The integrated stack is how it likely works.

## Next implementation target

Build a slow reference implementation with:
- `score_blockwise(plane)`
- `score_wholeplane(plane)`
- `score_hybrid(plane)`
- `reconcile_scores(local, global)`
- `project_output(result)`

That becomes the executable reference semantics for the substrate.
