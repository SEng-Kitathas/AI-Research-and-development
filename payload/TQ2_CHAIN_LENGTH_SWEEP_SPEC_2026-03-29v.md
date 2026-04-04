# TQ2 Chain-Length Sweep Spec
_Version: 2026-03-29v_

## Goal
Stress the current K2 latent-reuse operating band against increasing sequence depth.

## Method
- family-routing task
- synthetic sequence extension by cycling family code strings
- compare per-step explicit decode against K2 latent reuse

## Why this matters
Modern latent reasoning work warns that continuous / latent reasoning can degrade on longer chains.
This probe tests whether our current live band bends under depth.