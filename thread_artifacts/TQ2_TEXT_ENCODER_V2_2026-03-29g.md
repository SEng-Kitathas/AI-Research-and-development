# TQ2 Text Encoder v2
_Version: 2026-03-29g_

## Goal
Improve the first z80-inspired text probe without abandoning the cheap TQ2 substrate rules.

## Design
The encoder remains a single 3x3 ternary plane, but its rows are now semantically structured:

### Row 0 — Trigram hash coarse field
- cheap trigram accumulation
- hashed into 3 coarse buckets
- signed by simple local character features
- preserves typo-tolerant z80 spirit

### Row 1 — Lexical family block
- greeting/social signals
- identity/agency signals
- inner-state / threat / dream signals

### Row 2 — Structure block
- interrogative structure
- self-reference / pronoun pressure
- negation / risk polarity

## Rationale
v1 was too lossy because it forced everything through a flat trigram accumulator.
v2 preserves the same cheap arithmetic spirit but allocates explicit block structure for:
- local lexical motifs
- sentence form
- coarse semantic pressure

## Constraint
Still cheap:
- hash
- count
- sign
- clamp
- no floating point semantics inside the encoder