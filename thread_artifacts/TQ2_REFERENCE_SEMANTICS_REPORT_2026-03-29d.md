
# TQ2 Reference Semantics — Slow Lab Implementation
_Version: 2026-03-29d_

This artifact implements the integrated runtime doctrine:

**blockwise local pass → whole-plane global pass → hybrid reconciliation → projected output**

It is the executable semantics for the current TQ2 basis, not an optimized kernel.

## What is included

- `Block`
- `Plane`
- `Prototype`
- cheap closed transform family
- `score_blockwise(plane, prototypes)`
- `score_wholeplane(plane, prototypes)`
- `reconcile_scores(local, global)`
- `score_hybrid(plane, prototypes)`
- `project_output(result)`
- `integrated_infer(plane, prototypes)`

## Design rules preserved

All scoring remains inside the cheap closed operator family:
- shift
- permutation
- sign flip
- add / subtract
- clamp / projection
- lookup-driven transform selection

No generic heavy arithmetic is introduced.

## Representative demo cases

See `tq2_reference_semantics_demo_outputs_2026-03-29d.json` for concrete outputs.

The demo set intentionally includes:
- one **mixed/agreement** case
- one **local-first/disagreement** case
- one **global-first/disagreement** case

## Why this matters

This is the point where the substrate stops being just doctrine and becomes:
- inspectable
- replayable
- benchmarkable
- replaceable later with optimized kernels without changing semantics

## Next lab move

Use this reference semantics as the oracle for:
- RB-2A isolate
- RB-2B isolate
- RB-2C isolate
- RB-2R integrated runtime

Then run the mixed-task benchmark wave against the harness spec.
