# Weight Shadow Addendum
_Pass: 2026-03-29i_

## New promotion

### Sequence-Aware Text Encoder v3
Prompt state and emitted-prefix state are now represented separately within one 3x3 plane.
This materially improved the minimal next-character probe.

## Updated doctrine
**Sequence state is not optional metadata.**
For text-like behavior, it must be represented explicitly.

## Immediate consequence
Next sequence work should test:
- hidden-state carry block or second plane
- OOD + sequence together
- tiny free next-token behavior