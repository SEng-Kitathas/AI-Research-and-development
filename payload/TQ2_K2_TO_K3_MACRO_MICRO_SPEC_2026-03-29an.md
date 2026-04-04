# TQ2 K2→K3 Macro/Micro Track Test
_Version: 2026-03-29an_

## Goal
Test the user's macro/micro hypothesis:
derive K3 from filtered K2 aggregates rather than raw routine feed,
then use K3 only in late convergence.

## Variants
- BEST_CURRENT_STACK
- PERIODIC_K3_ALWAYS_LATE
- EVENT_K3_TRACK_LATE
- CFAR_K3_LATE_IF_CFAR
- CFAR_K3_FINAL_INTERP

## Framing
K2 = fast micro track
K3 = slow macro track built from selected K2 aggregate structure