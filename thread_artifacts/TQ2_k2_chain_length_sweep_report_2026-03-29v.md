# TQ2 K2 Latent-Reuse Chain-Length Sweep
_Version: 2026-03-29v_

This is the first direct chain-length stress test on the current live operating band.

## Why this exists
The process checkpoint said the biggest modern latent-reasoning risk we had not really stressed yet was:
- chain-length extrapolation
- whether latent-kept reasoning stays coherent as the reasoning path gets longer

So this sweep holds the branch concept fixed and increases synthetic sequence depth.

## Important caveat
This is still a synthetic family-routing stress test.
To extend depth beyond the natural terse family strings, the family code is **cycled**.
So this is not natural language generation.
It is a controlled latent-state retention probe.

## Compared strategies
- `PER_STEP_DECODE`
- `K2_LATENT_REUSE`

## Results

|   max_step | strategy        |   accuracy_pct |   macro_f1_pct |   n_examples |
|-----------:|:----------------|---------------:|---------------:|-------------:|
|          2 | PER_STEP_DECODE |          51.11 |          50.66 |           90 |
|          2 | K2_LATENT_REUSE |          37.78 |          34.37 |           90 |
|          4 | PER_STEP_DECODE |          62    |          61.54 |          150 |
|          4 | K2_LATENT_REUSE |          48    |          46.58 |          150 |
|          6 | PER_STEP_DECODE |          60.48 |          61.05 |          210 |
|          6 | K2_LATENT_REUSE |          56.67 |          56.05 |          210 |
|          8 | PER_STEP_DECODE |          60.37 |          60.55 |          270 |
|          8 | K2_LATENT_REUSE |          60.37 |          59.69 |          270 |
|         10 | PER_STEP_DECODE |          65.76 |          66    |          330 |
|         10 | K2_LATENT_REUSE |          61.82 |          60.85 |          330 |
|         12 | PER_STEP_DECODE |          62.82 |          62.78 |          390 |
|         12 | K2_LATENT_REUSE |          63.59 |          62.38 |          390 |

## Interpretation
The main thing to watch is whether K2 latent reuse bends earlier than per-step decode as depth rises.
If so, that tells us the current live operating band has a finite stability horizon under longer latent propagation.
