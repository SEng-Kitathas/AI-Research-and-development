# AI Research & Development — Geometric Inference

Research corpus for Tesseract Quaternion (TQ2) weight encoding and geometric reasoning systems.

## Core Focus

**TQ2 (Tesseract Quaternion v2)** — Geometric 9-state weight encoding using vpshufb inference. The canonical architecture for KarnOS/SYNAPSE neural substrate.

### Key Research Threads

- **Async Architecture Search** — Exploring asynchronous vs synchronous policy execution
- **A1 vs M2star Comparison** — Candidate architecture evaluation
- **Sigma V5** — Architecture-sensitive weight quantization
- **Local Refinement** — Fine-grained optimization passes

## Structure

```
├── payload/                    # Main research artifacts
│   ├── tq2_reference_*.py     # Reference implementations
│   ├── WEIGHT_SUBSTRATE_*     # White paper versions (v0.6 → v1.0)
│   ├── KarnOS-Shadow-*        # Shadow protocol docs
│   └── z80ai-main*            # Z80 AI integration research
├── audits/                     # CIL audit documents
├── experiments/                # Experiment results (JSON) and packages (ZIP)
├── thread_artifacts/           # Extracted conversation artifacts
├── HANDOFF_*                   # Project continuation protocols
└── manifest-sha256.txt         # Integrity verification
```

## Lineage

Part of the broader KarnOS/SYNAPSE/DEJI-NEAL ecosystem:
- GODSPEC v4.0.0 (Laws 7-14, fractal escalation, wave equation pheromones)
- Active Inference (Friston FEP) convergence proof
- CRHQ quantization system (CIL-Rahl Hierarchical Quantization)

---
*Weights ARE Memory (Axiom 4)*
