# TQ2 latent-kept + verification decode branch
_Version: 2026-03-29r_

This promotes the earlier latent-kept diagnostic into a real branch test.

The question is:
does this substrate prefer to keep reasoning in latent geometric family state and only collapse explicitly when needed?

## Calibrated verify strategy
- checkpoint interval: every **3** steps
- low-margin verification trigger: margin < **0.00**

## Results

| strategy             | task                    |   accuracy_pct |   macro_f1_pct |   relative_decode_cost |   n_examples |
|:---------------------|:------------------------|---------------:|---------------:|-----------------------:|-------------:|
| PER_STEP_DECODE      | stepwise family routing |          72.5  |          66.17 |                  1     |          120 |
| LATENT_DECODE_EVERY2 | stepwise family routing |          66.67 |          62.34 |                  0.542 |          120 |
| LATENT_DECODE_EVERY3 | stepwise family routing |          60    |          52.88 |                  0.375 |          120 |
| LATENT_VERIFY_DECODE | stepwise family routing |          72.5  |          66.17 |                  0.492 |          120 |
| LATENT_FINAL_ONLY    | final family decode     |          60    |          46.67 |                  1     |           25 |

## Interpretation

If sparse or adaptive decoding stays strong while decode cost falls, then the substrate is behaving more like a latent geometric reasoner than a tokenizer-style stepwise classifier.

If final-only remains best, that does not mean "never decode."
It means the system likely wants less frequent explicit collapse and better checkpoint / verification rules.
