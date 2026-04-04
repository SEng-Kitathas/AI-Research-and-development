# TQ2 Latent-Kept Sequence Pass
_Version: 2026-03-29q_

## Goal
Test the user's intuition that the current sequence process may be forcing a geometric reasoner to behave too much like a tokenizer.

## Idea
Keep more of the family decision in latent geometric state and decode less often.

## Variants
- per-step decode
- latent additive state, decoded every step
- latent state, decoded every 2 steps
- latent state, decoded only at final sequence state

## Constraint
This does not replace the current path.
It is a diagnostic pass to see whether less frequent discrete decoding helps.