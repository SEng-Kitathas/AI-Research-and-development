# TQ2 RegimeCache Inspiration Note
_Version: 2026-03-29l_

## Purpose
Translate the principle "stable expensive decisions may be reusable" into native TQ2 terms without conflating architectures.

## Native translation
If expensive routing or scoring outcomes remain stable across nearby sequence steps or strata, cache and reuse them rather than recomputing them every time.

## In TQ2 terms, candidates for reuse include
- regime choice
- prototype-family shortlist
- transform-family preference
- local/global arbitration path
- carry-route choice

## Guardrail
This is inspiration only.
It is not sparse attention, KV cache, or token index machinery imported into TQ2.

## Native name
**RegimeCache**