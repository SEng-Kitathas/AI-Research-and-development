# Weight Shadow Addendum
_Pass: 2026-03-29j_

## New promotion

### MultiPlane Sequence Encoder v4
A cheap two-plane prompt/carry split improves the minimal next-character probe over the single-plane sequence encoder.

## Updated doctrine
**Carry separation is worthwhile.**
Do not force prompt state and emitted-prefix state into one plane if a cheap two-plane split improves behavior.

## Immediate consequence
Next sequence work should test:
- tiny recurrence / prior-plane update
- OOD + sequence combined
- sequence-aware Forge metadata