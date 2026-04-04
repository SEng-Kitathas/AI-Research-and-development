# TQ2 Recursive Validation Pass
_Version: 2026-03-29al_

## Goal
Apply monotonic atomicity:
take the newest findings and recurse back through the earlier seam tests.

## This pass does two things
1. Larger-N rerun of LATENT_FINAL_ONLY using all current synthetic prompts/routes.
2. Recursive validation matrix comparing:
   - old pooled baseline
   - conservative family + scalar route
   - conservative family + wide interaction route

## Why
If the newest head design is genuinely better, it should survive contact with earlier seam tests instead of only looking good in one isolated pass.