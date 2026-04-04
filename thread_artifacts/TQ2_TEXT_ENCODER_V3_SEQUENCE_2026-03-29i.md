# TQ2 Sequence-Aware Text Encoder v3
_Version: 2026-03-29i_

## Goal
Address the weak next-character results by making prompt state and emitted-prefix state explicit.

## Layout
The encoder remains a single 3x3 ternary plane.

### Row 0 — Prompt coarse field
- trigram-hash coarse field over the prompt only

### Row 1 — Prompt profile block
- prompt structural/semantic pressure
- question-ness
- identity/inner-state pressure
- coarse vowel/consonant pressure

### Row 2 — Prefix progression block
- prefix length phase
- last-character class
- prefix hash drift

## Rationale
The prior "combined string" encoding smeared prompt and prefix into one surface.
v3 keeps the representation cheap but makes sequence state explicit.

## Constraint
Still cheap:
- hash
- count
- sign
- clamp
- no floating semantics