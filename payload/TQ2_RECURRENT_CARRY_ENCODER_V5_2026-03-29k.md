# TQ2 Recurrent Carry Encoder v5
_Version: 2026-03-29k_

## Goal
Test whether a tiny recurrent carry update improves next-character behavior beyond static prompt/prefix plane separation.

## Layout
- Plane A: prompt plane
- Plane B: prefix plane
- Plane C: recurrent carry plane

## Update
carry_t = clamp(carry_(t-1) + last-char block + prefix-progress block)

The carry plane is cheap, ternary-clamped, and updated once per emitted step.

## Rationale
Multi-plane v4 showed that explicit carry separation helps.
v5 asks whether a tiny recurrent update helps sequence scoring and propagation further.

## Constraint
Still cheap:
- hash
- count
- sign
- clamp
- no floating semantics