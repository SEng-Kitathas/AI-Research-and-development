# TQ2 Canonical Harness Tree Maintenance Note — 2026-04-04

## Purpose
This tree packages the recovered TQ2 evaluation stack into one authoritative working surface.

## Selection rule used
Chosen files were selected by operational centrality, not by novelty.
The decisive rule was:
1. prefer files that recovered runners actually import or depend on
2. prefer files with matching result JSONs and audit lineage
3. keep ancestral/lineage variants only as explicit non-canonical references

## Canonical selections

### Authoritative semantics module
- `src/tq2_reference_semantics.py`
- source lineage: `tq2_reference_semantics_v2_2026-03-29e.py`

Why:
- recovered runners depend on this version in practice
- it sits at the operational center of the restored stack
- it is the best current anchor for replay and controlled mutation

### Canonical harness set
- `harness/async_arch_search_runner.py`
- `harness/a1_vs_m2star_runner.py`
- `harness/a1_local_refinement_runner.py`
- `harness/v5_async_refine_runner.py`

Why:
- these represent the recovered search → compare → refine ladder
- they encode the main design pressure already surfaced by the corpus

### Results pinned
- async arch search
- A1 vs M2*
- A1 local refinement
- sigma-v5 architecture-sensitive result
- v5 async winner local refinement

## Ancestral / lineage files retained
- `src/tq2_reference_semantics_v1_ancestral.py`
- `src/tq2_reference_semantics_v3_lineage.py`

These are preserved for branch archaeology and future controlled comparison, but they are not the active canonical import target.

## Load-bearing design findings pinned by this tree
- async decomposition is real signal
- A1 is the best recovered aggregate architecture over sigma v2/v3/v4
- sigma-v5 breaks naive async supremacy
- resolver + sync mode are load-bearing controls
- surface-aware integration law matters more than generic async branding

## Canonical replay order
1. async_arch_search_runner.py
2. a1_vs_m2star_runner.py
3. a1_local_refinement_runner.py
4. v5_async_refine_runner.py

## Warning
This tree is canonical only relative to the currently recovered corpus.
Future promotion requires explicit supersession, not silent replacement.
