# TQ2 Conservative-to-Speculative Dyno Sweep
_Version: 2026-03-29t_

## Goal
Push the latent-kept branch from conservative to speculative and see where it locks in or collapses.

## Calibrated moderate verify settings
- checkpoint interval: every **2** steps
- low-margin verification trigger: margin < **0.00**

## Variants
- CONSERVATIVE_FULL: full family eval + explicit decode every step
- MODERATE_VERIFY: shortlist reuse + checkpointed / low-margin verify
- AGGRESSIVE_SPARSE_K2: top-2 shortlist reuse, decode only on k=2 refresh
- AGGRESSIVE_SPARSE_K3: top-2 shortlist reuse, decode only on k=3 refresh
- SPECULATIVE_REUSE_VERIFY: k=3 shortlist reuse + verify/decode on disagreement or low margin
- SPECULATIVE_REUSE_K3: k=3 shortlist reuse with no extra verification