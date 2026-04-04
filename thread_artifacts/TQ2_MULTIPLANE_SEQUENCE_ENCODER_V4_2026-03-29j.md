# TQ2 MultiPlane Sequence Encoder v4
_Version: 2026-03-29j_

## Goal
Test whether explicit cheap two-plane carry structure helps more than forcing sequence state into a single plane.

## Layout

### Plane A — Prompt plane
- prompt trigram coarse field
- prompt profile block
- prompt shape pressure

### Plane B — Prefix/carry plane
- prefix trigram coarse field
- prefix progression block
- prefix character-class block

## Rationale
Single-plane sequence encoding improved things, but sequence remained weak.
A cheap two-plane split tests whether separating prompt state from emitted-prefix state improves next-step behavior without leaving the TQ2 family.

## Constraint
Still cheap:
- hash
- count
- sign
- clamp
- per-plane transform scoring
- no floating semantics