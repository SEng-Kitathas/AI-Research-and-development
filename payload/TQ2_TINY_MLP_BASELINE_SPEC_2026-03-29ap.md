# TQ2 Tiny MLP Baseline on T1–T4
_Version: 2026-03-29ap_

## Goal
Provide an external calibration point for T1–T4 using a small learned baseline.

## Important scope note
This baseline is run on a transparent, harness-consistent reconstruction of the T1–T4 task families:
- T1 whole-plane motif invariance
- T2 block composition invariance
- T3 majority-sign sanity
- T4 mixed global+local motifs

It is not a byte-identical rerun of the earlier hidden harness implementation.
It is an external comparator over the same task family semantics.

## Model
- input: flattened 3x3 ternary plane
- scaler + MLPClassifier(hidden_layer_sizes=(16,), activation=tanh)
- 20 random seeds