# TQ2 Latent-Kept + Verification Decode Branch
_Version: 2026-03-29r_

## Goal
Promote the latent-kept diagnostic into a real test branch:
- keep family/routing state latent by default
- surface explicit family decisions only on checkpoints or instability

## Calibrated verify strategy
- checkpoint interval: every **3** steps
- low-margin verification trigger: margin < **0.00**

## Variants
- per-step decode
- sparse decode every 2 or 3 steps
- latent verify decode (checkpoint + low-margin + top-family change)
- final-only decode as upper-bound sequence diagnostic

## Constraint
This remains native TQ2 family routing, not imported token hidden-state machinery.