# TQ2 Carry-Drift Abstention Note
_Version: 2026-03-29p_

## Purpose
Make abstention depend on both:
- low confidence margin
- high carry-state movement

## Calibrated parameters
- Full recompute: margin<2.30 and drift>=0
- Refresh/reuse: margin<2.30 and drift>=0

## Principle
A stateful sequence system should hesitate more when its internal carry is moving sharply.