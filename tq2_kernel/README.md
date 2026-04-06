# TQ2 Canonical Harness Tree

This directory is the cleaned canonical replay surface extracted from the recovered geometric inference corpus.

## Layout
- `src/` — semantics modules
- `harness/` — recovered runner ladder
- `results/` — pinned recovered result JSONs
- `docs/` — maintenance note and summary

## Canonical import target
Use `src/tq2_reference_semantics.py` unless and until explicitly superseded.

## Replay ladder
1. `harness/async_arch_search_runner.py`
2. `harness/a1_vs_m2star_runner.py`
3. `harness/a1_local_refinement_runner.py`
4. `harness/v5_async_refine_runner.py`
