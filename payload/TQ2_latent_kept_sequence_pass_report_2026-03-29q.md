# TQ2 latent-kept sequence pass
_Version: 2026-03-29q_

This tests the user's intuition that the current pipeline may be snapping a geometric reasoner into tokenizer-like decisions too often.

## Strategies

- `PER_STEP_DECODE`: fully decode family state every step
- `LATENT_KEPT_ADDITIVE`: maintain latent family state across steps, but still decode each step
- `LATENT_DECODE_EVERY2`: maintain latent family state, decode only every 2 steps
- `LATENT_FINAL_ONLY`: keep family state latent through the whole sequence and decode only at the end

## Results

| strategy             |   accuracy_pct |   macro_f1_pct |   relative_decode_cost |   n_examples |
|:---------------------|---------------:|---------------:|-----------------------:|-------------:|
| PER_STEP_DECODE      |          57.87 |          54.96 |                   1    |          216 |
| LATENT_KEPT_ADDITIVE |          70.37 |          63.06 |                   1    |          216 |
| LATENT_DECODE_EVERY2 |          64.81 |          59.52 |                   0.75 |          216 |
| LATENT_FINAL_ONLY    |          82.22 |          81.43 |                   0.55 |           45 |

## Interpretation

This is not a new architecture.
It is a diagnostic pass.

If less frequent decoding helps, then the current sequence handling may indeed be forcing the substrate into too tokenizer-like a mode.
If it does not help, then the main issue lies elsewhere.
