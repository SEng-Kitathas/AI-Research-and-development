# TQ2 / CIL Full Corpus Extraction
_Extracted: 2026-03-29 | Source: TQ2_CIL_FULL_THREAD_ARTIFACTS_2026-03-29af.zip | 147 files_

---

## LAYER 1 — OIE Triple Extraction
> Every stated fact decomposed into (Subject, Predicate, Object) triples. No filtering applied.

### 1.1 Architecture / Substrate Facts

| Subject | Predicate | Object |
|---|---|---|
| TQ2 | is | canonical geometric reasoning substrate |
| TQ2 primitive domain | is | T = {-1, 0, 1} |
| TQ2 canonical plane | is | 3×3 ternary grid (9 cells) composed of 3 ordered blocks |
| TQ2 canonical block | is | 1×3 ordered ternary strip |
| RB-2A | is | whole-plane transform branch |
| RB-2B | is | blockwise transform branch |
| RB-2C | is | hybrid transform branch |
| RB-2R | is | integrated runtime composition of RB-2A + RB-2B + RB-2C |
| RB-2R_v3 | is | current best integrated runtime candidate |
| CIL | stands for | Cognitive Intersymbolic Ledger |
| CIL | is | native exact memory substrate and persistent ledger core |
| Exact Plane | is | truth-preserving reversible provenance-bearing layer |
| Representational Plane | is | compressed geometric family-forming prediction-supporting layer |
| Legal transforms (whole-plane) | include | identity, 90°/180°/270° rotation, horizontal reflection, vertical reflection, optional diagonal reflections |
| Legal transforms (blockwise) | include | identity, left cyclic shift, right cyclic shift, optional signed inversion |
| Legal operators (all) | are | shift, permutation, sign flip, add/subtract, clamp/projection, lookup |
| Radical | has | prototype plane, legal transform family, semantic metadata |
| Radical promotion ladder | is | Seed → Mined → Apex |
| Apex radical | requires | residual reduction, normalization/isomorphism stability, recurrence, contradiction survival, provenance quality |
| K2 Reuse | is | fast two-family shortlist lane refreshed every 2 steps |
| K3 Meta Lane | is | slower broader shortlist lane refreshed every 3 steps |
| RegimeCache | is | inspiration-only term; native meaning is short-horizon refresh-vs-reuse scheduling |
| Latent-Kept Reasoning | is | regime where family/route state remains latent by default; explicit collapse only on demand |
| Explicit Collapse | is | any discrete surfaced decision such as family decode or routed symbolic output |
| Verification Decode | is | explicit collapse triggered by checkpoint, instability, disagreement, or output demand |
| Carry | is | cheap recurrent latent state propagated across steps |
| Carry Drift | is | magnitude of change in carry state between adjacent steps |
| CIL memory layers | include | Session Buffer, Episodic Layer, Semantic Layer, Vector/Neighborhood Layer, Integrity Layer |
| CIL functional layers | include | Consolidation Engine, Replay/Sleep layer, Retrieval Compiler, Archive/Audit layer |
| Consolidation Engine | is | center of gravity for memory formation |
| Geometry / Topology | serves as | replay topology, family locality, retrieval clustering, recurrence vs novelty exposure, compaction ordering |
| Retrieval Compiler | compiles | working packet, evidence packet, contradiction packet, compressed family packet |
| Recurrent Carry v5 | is | current best minimal sequence probe setup |

---

### 1.2 All Benchmark Results — Raw Numeric Extraction

#### RB-2R Wave v1 (TQ2_RB2R_mixed_task_wave_report_2026-03-29d)
| Task | Model | Accuracy % | Macro F1 % |
|---|---|---|---|
| T1 Whole-plane motif invariance | BASE-0 | 61.56 | 58.88 |
| T1 Whole-plane motif invariance | RB-2A | 97.12 | 97.06 |
| T1 Whole-plane motif invariance | RB-2B | 47.12 | 42.79 |
| T1 Whole-plane motif invariance | RB-2R | 70.69 | 63.86 |
| T2 Block composition invariance | BASE-0 | 76.75 | 72.83 |
| T2 Block composition invariance | RB-2A | 80.19 | 77.65 |
| T2 Block composition invariance | RB-2B | 100.00 | 100.00 |
| T2 Block composition invariance | RB-2R | 99.94 | 99.94 |
| T3 Majority-sign sanity | BASE-0 | 82.94 | 60.85 |
| T3 Majority-sign sanity | RB-2A | 82.94 | 60.85 |
| T3 Majority-sign sanity | RB-2B | 40.44 | 19.14 |
| T3 Majority-sign sanity | RB-2R | 40.44 | 19.14 |
| T4 Mixed global+local motifs | BASE-0 | 35.75 | 32.96 |
| T4 Mixed global+local motifs | RB-2A | 53.12 | 44.94 |
| T4 Mixed global+local motifs | RB-2B | 36.75 | 24.17 |
| T4 Mixed global+local motifs | RB-2R | 48.25 | 39.09 |

#### RB-2R Wave v2 (TQ2_RB2R_v2_mixed_task_wave_report_2026-03-29e)
| Task | Model | Accuracy % | Macro F1 % |
|---|---|---|---|
| T1 | RB-2R_v2 | 70.62 | 64.20 |
| T2 | RB-2R_v2 | 100.00 | 100.00 |
| T3 | RB-2R_v2 | 77.75 | 57.29 |
| T4 | RB-2R_v2 | 53.50 | 45.65 |

#### RB-2R Wave v3 (TQ2_RB2R_v3_mixed_task_wave_report_2026-03-29f)
| Task | Model | Accuracy % | Macro F1 % |
|---|---|---|---|
| T1 | RB-2R_v3 | 97.12 | 97.06 |
| T2 | RB-2R_v3 | 100.00 | 100.00 |
| T3 | RB-2R_v3 | 100.00 | 100.00 |
| T4 | RB-2R_v3 | 53.50 | 45.65 |

#### Substrate Probe (TQ2_substrate_probe_report)
| Task | Model | Accuracy % | Std % |
|---|---|---|---|
| Whole-plane invariant motif | Baseline | 49.58 | 3.07 |
| Whole-plane invariant motif | WholeTransform | 94.22 | 3.88 |
| Whole-plane invariant motif | Blockwise | 48.39 | 6.77 |
| Block-composition invariant | Baseline | 93.64 | 1.39 |
| Block-composition invariant | WholeTransform | 77.72 | 8.53 |
| Block-composition invariant | Blockwise | 93.64 | 1.39 |
| Majority-sign baseline | Baseline | 92.08 | 3.78 |
| Majority-sign baseline | WholeTransform | 75.53 | 9.05 |
| Majority-sign baseline | Blockwise | 93.89 | 5.52 |

#### Latent-Kept Sequence Pass (TQ2_latent_kept_sequence_pass_report_2026-03-29q)
| Strategy | Accuracy % | Macro F1 % | Relative Decode Cost | N |
|---|---|---|---|---|
| PER_STEP_DECODE | 57.87 | 54.96 | 1.00 | 216 |
| LATENT_KEPT_ADDITIVE | 70.37 | 63.06 | 1.00 | 216 |
| LATENT_DECODE_EVERY2 | 64.81 | 59.52 | 0.75 | 216 |
| LATENT_FINAL_ONLY | 82.22 | 81.43 | 0.55 | 45 |

#### Latent Verify Branch (TQ2_latent_verify_branch_report_2026-03-29r)
| Strategy | Task | Accuracy % | Macro F1 % | Relative Decode Cost | N |
|---|---|---|---|---|---|
| PER_STEP_DECODE | stepwise family routing | 72.50 | 66.17 | 1.000 | 120 |
| LATENT_DECODE_EVERY2 | stepwise family routing | 66.67 | 62.34 | 0.542 | 120 |
| LATENT_DECODE_EVERY3 | stepwise family routing | 60.00 | 52.88 | 0.375 | 120 |
| LATENT_VERIFY_DECODE | stepwise family routing | 72.50 | 66.17 | 0.492 | 120 |
| LATENT_FINAL_ONLY | final family decode | 60.00 | 46.67 | 1.000 | 25 |

#### Dyno Sweep (TQ2_dyno_sweep_report_2026-03-29t)
| Variant | Accuracy % | Macro F1 % | Rel. Score Cost | Rel. Decode Cost | Efficiency Index |
|---|---|---|---|---|---|
| CONSERVATIVE_FULL | 72.50 | 66.17 | 1.000 | 1.000 | 0.706 |
| MODERATE_VERIFY | 55.00 | 53.63 | 0.725 | 0.542 | 0.826 |
| AGGRESSIVE_SPARSE_K2 | 55.00 | 53.63 | 0.725 | 0.542 | 0.826 |
| AGGRESSIVE_SPARSE_K3 | 34.17 | 33.70 | 0.625 | 0.375 | 0.633 |
| SPECULATIVE_REUSE_VERIFY | 38.33 | 39.14 | 0.650 | 0.525 | 0.636 |
| SPECULATIVE_REUSE_K3 | 38.33 | 39.14 | 0.650 | 0.525 | 0.636 |

#### K2 Chain-Length Sweep (TQ2_k2_chain_length_sweep_report_2026-03-29v)
| Max Step | Strategy | Accuracy % | Macro F1 % | N |
|---|---|---|---|---|
| 2 | PER_STEP_DECODE | 51.11 | 50.66 | 90 |
| 2 | K2_LATENT_REUSE | 37.78 | 34.37 | 90 |
| 4 | PER_STEP_DECODE | 62.00 | 61.54 | 150 |
| 4 | K2_LATENT_REUSE | 48.00 | 46.58 | 150 |
| 6 | PER_STEP_DECODE | 60.48 | 61.05 | 210 |
| 6 | K2_LATENT_REUSE | 56.67 | 56.05 | 210 |
| 8 | PER_STEP_DECODE | 60.37 | 60.55 | 270 |
| 8 | K2_LATENT_REUSE | 60.37 | 59.69 | 270 |
| 10 | PER_STEP_DECODE | 65.76 | 66.00 | 330 |
| 10 | K2_LATENT_REUSE | 61.82 | 60.85 | 330 |
| 12 | PER_STEP_DECODE | 62.82 | 62.78 | 390 |
| 12 | K2_LATENT_REUSE | 63.59 | 62.38 | 390 |

#### Offset K2/K3 Sweep (TQ2_offset_k2_k3_report_2026-03-29w)
| Variant | Accuracy % | Macro F1 % | Rel. Score Cost | Rel. Decode Cost | Meta Refreshes | Fast Refreshes |
|---|---|---|---|---|---|---|
| K2_BASE | 50.69 | 49.53 | 0.725 | 1.00 | 0 | 78 |
| OFFSET_K2_FAST_K3_META | 34.03 | 34.96 | 0.883 | 1.00 | 54 | 78 |
| FED_K3_TO_K2 | 34.03 | 34.96 | 0.883 | 1.00 | 54 | 78 |
| STAGGERED_23 | 34.03 | 34.51 | 0.683 | 1.00 | 54 | 78 |

#### K2→K3 Summary Lane (TQ2_k2_to_k3_summary_report_2026-03-29x)
| Variant | Accuracy % | Macro F1 % | Rel. Score Cost | Meta Updates | Fast Updates |
|---|---|---|---|---|---|
| K2_BASE | 50.69 | 49.53 | 0.725 | 0 | 78 |
| K2_TO_K3_SUMMARY | 50.69 | 49.53 | 0.725 | 54 | 78 |
| K2_TO_K3_SUMMARY_FEEDBACK_CHECKPOINT | 50.69 | 49.53 | 0.692 | 54 | 78 |

#### Adaptive K2 Sweep (TQ2_adaptive_k2_sweep_report_2026-03-29y)
| Variant | Accuracy % | Macro F1 % | Rel. Score Cost | Rel. Decode Cost | Adaptive Events |
|---|---|---|---|---|---|
| FIXED_K2 | 50.69 | 49.53 | 0.725 | 0.542 | 0 |
| ADAPTIVE_EASY_HARD | 50.69 | 49.53 | 0.725 | 0.806 | 62 |
| ADAPTIVE_VERIFY_ONLY | 50.69 | 49.53 | 0.725 | 0.542 | 48 |
| ADAPTIVE_HIGH_COMPRESSION | 50.69 | 49.53 | 0.725 | 0.451 | 105 |

#### Multi-Path Latent Benchmark (TQ2_multi_path_latent_benchmark_report_2026-03-29z)
| Metric | Accuracy % | Macro F1 % | N |
|---|---|---|---|
| PER_STEP_FAMILY | 52.08 | 52.29 | 288 |
| K2_FAMILY | 30.90 | 32.18 | 288 |
| PER_STEP_ROUTE_PROBE | 41.32 | 40.26 | 288 |
| K2_ROUTE_PROBE | 24.31 | 25.07 | 288 |

#### Adaptive Multi-Path Rerun (TQ2_adaptive_multi_path_rerun_report_2026-03-29aa)
| Metric | Accuracy % | Macro F1 % | N |
|---|---|---|---|
| PER_STEP_FAMILY | 52.08 | 52.29 | 288 |
| K2_FAMILY | 32.99 | 34.63 | 288 |
| ADAPTIVE_K2_FAMILY | 32.99 | 34.63 | 288 |
| PER_STEP_ROUTE_PROBE | 41.32 | 40.26 | 288 |
| K2_ROUTE_PROBE | 24.31 | 25.07 | 288 |
| ADAPTIVE_K2_ROUTE_PROBE | 24.31 | 25.07 | 288 |

#### Latent State Probe — Summary (TQ2_latent_state_probe_report_2026-03-29ab)
| Mode | Family Probe Acc % | Route Probe Acc % | Route Sep Gap |
|---|---|---|---|
| per_step | 51.04 | 58.61 | 0.589 |
| k2 | 46.53 | 54.17 | 1.181 |
| adaptive_k2 | 46.53 | 54.17 | 1.181 |

#### Latent State Probe — Stepwise Route Probe
| Mode | Step | Route Probe Acc % | Route Sep Gap |
|---|---|---|---|
| per_step | 0 | 50.00 | 0.000 |
| per_step | 1 | 80.00 | 4.692 |
| per_step | 2 | 88.33 | 2.442 |
| per_step | 3 | 63.89 | 0.263 |
| per_step | 4 | 75.00 | 0.646 |
| per_step | 5 | 79.17 | 2.394 |
| per_step | 6 | 83.33 | 1.274 |
| per_step | 7 | 100.00 | 0.532 |
| k2 | 0 | 50.00 | 0.000 |
| k2 | 1 | 63.33 | 0.591 |
| k2 | 2 | 70.00 | 1.803 |
| k2 | 3 | 77.78 | 9.699 |
| k2 | 4 | 87.50 | 14.400 |
| k2 | 5 | 87.50 | 14.962 |
| k2 | 6 | 100.00 | 28.333 |
| k2 | 7 | 100.00 | 21.216 |
| adaptive_k2 | 0–7 | identical to k2 | identical to k2 |

#### Latent Criticality Map (TQ2_latent_criticality_map_report_2026-03-29af)
Baseline probe (used in criticality map — NOTE: different from ab probe numbers):
| Mode | Family Probe Acc % | Route Probe Acc % |
|---|---|---|
| per_step | 51.04 | 31.60 |
| k2 | 46.53 | 27.43 |
| adaptive_k2 | 46.53 | 27.43 |

Single-dimension ablation results:
| Ablated Dim | Family Acc Drop | Route Acc Drop | Total Drop Score |
|---|---|---|---|
| z_YES | 0.0556 | 0.0347 | **0.0903** (most critical) |
| z_HI | 0.0312 | 0.0069 | 0.0382 |
| z_NO | 0.0347 | −0.0243 | 0.0104 |
| z_UNKNOWN | 0.0208 | −0.0139 | 0.0069 |
| z_MAYBE | −0.0243 | −0.0069 | **−0.0312** (slightly improves when removed) |

#### Route-Aware / Dual-Head Readout (TQ2_route_aware_dual_head_report_2026-03-29ae)
| Metric | Accuracy % | Macro F1 % | N |
|---|---|---|---|
| FAMILY_ONLY_FAMILY | 52.08 | 52.29 | 288 |
| FAMILY_ONLY_ROUTE | 41.32 | 40.26 | 288 |
| DUAL_HEAD_FAMILY | 52.08 | 52.29 | 288 |
| DUAL_HEAD_ROUTE | 41.32 | 40.26 | 288 |

#### Z80 Text Probe (TQ2_z80_text_probe_report_2026-03-29f)
| Model | Accuracy % | Macro F1 % | N |
|---|---|---|---|
| BASE-0 | 52.78 | 47.76 | 36 |
| RB-2A | 41.67 | 38.97 | 36 |
| RB-2B | 52.78 | 50.79 | 36 |
| RB-2R_v2 | 55.56 | 54.84 | 36 |
| RB-2R_v3 | 55.56 | 54.84 | 36 |

#### Minimal Next-Char Probe v1 (TQ2_minimal_nextchar_probe_report_2026-03-29h)
| Model | Accuracy % | Macro F1 % | N |
|---|---|---|---|
| BASE-0 | 12.96 | 7.99 | 216 |
| RB-2A | 12.50 | 6.31 | 216 |
| RB-2B | 8.33 | 4.56 | 216 |
| RB-2R_v3 | 11.11 | 5.74 | 216 |

#### Next-Char Encoder v2 vs Sequence-Aware v3 (TQ2_nextchar_encoder_v2_v3_report_2026-03-29i)
| Encoder | Model | Accuracy % | Macro F1 % | N |
|---|---|---|---|---|
| combined_v2 | BASE-0 | 12.96 | 7.99 | 216 |
| combined_v2 | RB-2A | 12.50 | 6.31 | 216 |
| combined_v2 | RB-2B | 8.33 | 4.56 | 216 |
| combined_v2 | RB-2R_v3 | 11.11 | 5.74 | 216 |
| sequence_v3 | BASE-0 | 18.52 | 14.99 | 216 |
| sequence_v3 | RB-2A | 16.67 | 14.94 | 216 |
| sequence_v3 | RB-2B | 10.65 | 8.77 | 216 |
| sequence_v3 | RB-2R_v3 | 13.43 | 12.19 | 216 |

#### Single-Plane v3 vs Multi-Plane v4 (TQ2_nextchar_singleplane_v3_vs_multiplane_v4_report_2026-03-29j)
| Encoder | Model | Accuracy % | Macro F1 % | N |
|---|---|---|---|---|
| singleplane_v3 | BASE-0 | 19.44 | 15.45 | 216 |
| singleplane_v3 | RB-2A | 15.28 | 12.66 | 216 |
| singleplane_v3 | RB-2R_v3 | 12.04 | 10.71 | 216 |
| multiplane_v4 | BASE-0_MP | 37.96 | 39.76 | 216 |
| multiplane_v4 | RB-2A_MP | 30.09 | 32.92 | 216 |
| multiplane_v4 | RB-2R_v3_MP | 20.83 | 22.54 | 216 |

#### Multi-Plane v4 vs Recurrent Carry v5 (TQ2_nextchar_multiplane_v4_vs_recurrent_v5_report_2026-03-29k)
| Encoder | Model | Accuracy % | Macro F1 % | N |
|---|---|---|---|---|
| multiplane_v4 | BASE-0_MP | 37.96 | 39.76 | 216 |
| multiplane_v4 | RB-2R_v3_MP | 20.83 | 22.54 | 216 |
| recurrent_v5 | BASE-0_REC | 37.96 | 41.03 | 216 |
| recurrent_v5 | RB-2R_v5_REC | 30.09 | 31.60 | 216 |

#### Recurrent Refresh-vs-Reuse Probe (TQ2_recurrent_refresh_reuse_probe_2026-03-29l)
| Strategy | Accuracy % | Macro F1 % | Relative Scoring Cost |
|---|---|---|---|
| FULL_REC | 30.09 | 31.60 | 1.000 |
| REFRESH2_TOP2 | 28.24 | 27.85 | 0.571 |
| REFRESH3_TOP2 | 20.37 | 17.65 | 0.429 |
| REFRESH2_TOP3 | 28.24 | 27.98 | 0.607 |

#### OOD + Recurrence + Refresh Probe (TQ2_ood_recurrence_refresh_probe_2026-03-29m)
| Strategy | Accuracy % | Macro F1 % | Unknown Overcommit % | Rel. Scoring Cost |
|---|---|---|---|---|
| FULL_FAM | 57.87 | 54.96 | 45.83 | 1.00 |
| FULL_FAM_OOD | 50.00 | 35.36 | 11.11 | 1.00 |
| RR2_TOP2_FAM | 57.87 | 54.96 | 45.83 | 0.70 |
| RR2_TOP2_FAM_OOD | 46.30 | 32.78 | 22.22 | 0.70 |

---

## LAYER 2 — ELT Raw State Capture
> All assumptions, all tensions, all triggers, preserved without filtering.

### 2.1 Current Doctrine (Settled)
- TQ2 is the canonical geometric reasoning substrate
- CIL is the native exact memory substrate / persistent ledger core
- Latent-Kept Reasoning is a live branch
- K2 is the current live fast lane for latent family-state updates
- K3 belongs in summary/checkpoint/audit/cold-state duty, NOT live control
- Exact Plane / Representational Plane is the standing dual-plane contract
- RB-2R_v3 is the current best integrated runtime candidate

### 2.2 Explicitly NOT Settled
- Best explicit-collapse / verification policy
- Best adaptive compression signal
- Whether current readout is the main bottleneck
- Whether route diversity is preserved well enough for real use
- Whether K3 has a stronger future role than meta-duty

### 2.3 Full Assumption Register
| ID | Assumption | Status | Key Evidence | Revisit Triggers |
|---|---|---|---|---|
| A-001 | Latent-kept reasoning is structurally better than constant token-like explicit collapse | Supported, under active test | Latent-kept diagnostic improved strongly over per-step decode; LATENT_VERIFY_DECODE matches PER_STEP at 0.492 decode cost | Chain-length degradation beyond fixed-collapse baseline; multi-path collapse not repairable by better readout |
| A-002 | K2 is the correct live operating band | Supported as best current band | Fixed K2 outperformed K3-style sparse reuse; offset K2/K3 hurt; K2→K3 summary was neutral | Adaptive K2 underperforms consistently on harder chain/route tasks |
| A-003 | K3 should be summary/checkpoint/audit/cold-state, NOT live controller | Supported | K3-as-controller hurt; K2→K3 summary was neutral/cost-positive; offset K2/K3 dropped from 50.69% to 34.03% | K3 shows value in bridge/memory/replay role |
| A-004 | Adaptive compression/collapse is a real knob class | Conceptually supported, weakly realized | Research literature supports adaptive latent compression; adaptive K2 found a regime reducing decode cost; margin-only adaptive did NOT improve quality | Richer control signals (route pressure, disagreement, carry drift, chain position) fail to beat fixed K2 |
| A-005 | The latent state contains more structure than current readout uses | Strengthened | Route-probe behavior was weak; latent-state centroid probing showed route separability still present in latent vectors | Stronger probes show route structure is actually not robust; improved readout fails to recover performance |

### 2.4 Full Tension / Contradiction Log
| ID | Tension | Best Interpretation | Must Revisit |
|---|---|---|---|
| T-001 | Route-probe results implied route collapse, but latent-state probe showed route structure survives | Current readout likely collapses valid route structure too early | All statements equating poor route-probe accuracy with absent latent route information |
| T-002 | Adaptive K2 is conceptually supported by outside work but margin-only adaptive control did NOT improve quality | The knob class is real; the control signal is weak | Any claim that adaptivity itself was disproven |
| T-003 | K3 summary lane is conceptually sane but empirically neutral | K3 belongs to slower summary/checkpoint or memory-tier duty, NOT live control | Whether K3 should appear in the live reasoning loop vs memory/replay/bridge loops |
| T-004 | Behavior-level route probes were weak; latent-state centroid probes suggest route structure survives | Current family-level readout may be collapsing route structure too early | All conclusions focusing only on collapse timing rather than readout/disentangling |

### 2.5 Full Revisit Trigger Register
| Class | Trigger | What to Revisit |
|---|---|---|
| R1 | Better readout (route-aware or dual-head) tested | Route-collapse conclusions; adaptive-collapse conclusions; K2 vs per-step comparisons |
| R2 | Stronger latent probes reveal poor route/family separation | "Latent state is richer than readout" conclusion |
| R3 | Criticality map shows only a subset of planes/routes/dimensions carry the signal | Substrate-wide assumptions; whether current latent vector is too entangled |
| R4 | Bridge / hot-cold memory tests make K3 or slower summary state valuable | K3 doctrine; ontology around meta-lane vs memory-tier role |
| R5 | Adaptive or fixed K2 breaks on more realistic long-horizon tasks | Latent-kept doctrine strength; current optimism about live operating band |
| R6 | Route-aware or dual-head readout recovers family or route behavior | All conclusions that blamed latent-state quality alone; promote readout/disentangling over raw collapse timing |
| R7 | One or two latent dimensions dominate family or route probe performance | Whether current latent vector is overly entangled; whether readout should be dimension-selective rather than fully pooled |

---

## LAYER 3 — Systematic Review Extraction
> Standardized form applied uniformly across all experimental documents.

### 3.1 Per-Experiment Extraction Table

| Experiment | Version | What Changed | Best Result | Failure Mode Found | Doctrine Impact | Next Step Triggered |
|---|---|---|---|---|---|---|
| Substrate Probe | initial | First test of WholeTransform vs Blockwise vs Baseline | WholeTransform 94.22% on T1; Blockwise 93.64% on T2 | Neither branch universal | Both branches are real; no single operator family | Formalize object grammar |
| RB-2R Wave v1 | 2026-03-29d | First integrated runtime test | RB-2A 97.12% T1; RB-2B 100% T2 | RB-2R collapsed on T3 (40.44%); T4 not yet won | Composition idea plausible; fusion logic needs work | Build RB-2R_v2 with sanity fallback |
| RB-2R Wave v2 | 2026-03-29e | Added sanity fallback, margin confidence, asymmetric thresholds | T3 fixed to 77.75%; T4 at 53.50% (edging RB-2A) | T1 still taxed (70.62% vs RB-2A 97.12%) | Composition justified enough to keep; not fully solved | Build RB-2R_v3 with mode gating |
| RB-2R Wave v3 | 2026-03-29f | Metadata-aware mode gating | T1 97.12% (matches RB-2A); T2 100%; T3 100%; T4 53.50% | T4 still only slightly ahead of RB-2A | RB-2R_v3 is first promotable integrated runtime | Validate on less synthetic tasks; decide metadata routing scope |
| Z80 Text Probe | 2026-03-29f | First text-domain test | RB-2R_v3 55.56% on intent classification | RB-2A weakest at 41.67%; absolute accuracy too low | Text is new pressure seam; runtime survives first contact | Improve text-to-plane encoder |
| Minimal Next-Char v1 | 2026-03-29h | First autoregressive-style probe | Best: BASE-0 12.96% (all models near floor) | All models near floor | Sequence continuation is a harder problem; encoder/runtime have work to do | Sequence-aware representation is the next seam |
| Encoder v2 vs v3 | 2026-03-29i | Kept prompt/prefix structurally distinct inside plane | sequence_v3 BASE-0 18.52%; RB-2R_v3 13.43% | Scores still modest | Representation was bottleneck on next-char task | Add carry block or second plane |
| Single-plane v3 vs Multi-plane v4 | 2026-03-29j | Explicit carry separation (Plane A prompt, Plane B prefix/carry) | multiplane_v4 BASE-0_MP 37.96%; RB-2R_v3_MP 20.83% | RB-2R still loses to simple baseline | Carry separation is worthwhile; BASE-0 benefits too | Add recurrent update |
| Multi-plane v4 vs Recurrent v5 | 2026-03-29k | Added cheap ternary recurrent carry plane update | recurrent_v5 RB-2R_v5_REC 30.09% | BASE-0_REC still ties multiplane_v4 best | Sequence propagation is now visibly beneficial; recurrent v5 is current best sequence setup | Combine OOD + recurrence |
| Recurrent Refresh-vs-Reuse | 2026-03-29l | First native RegimeCache translation; tested shortlist reuse vs full recompute | REFRESH2_TOP2 28.24% at 0.571 cost (vs FULL_REC 30.09% at 1.0) | Aggressive REFRESH3 drops to 20.37% | REFRESH2_TOP2 preserves most performance at 43% cost reduction | OOD + refresh + recurrence combined test |
| OOD + Recurrence + Refresh | 2026-03-29m | Combined all three seams | RR2_TOP2_FAM matches FULL_FAM at 57.87% at 0.70 cost | OOD threshold causes accuracy drop (46.30%) and overcommit not fully resolved | Refresh/reuse viable under OOD pressure; OOD+reuse interaction needs redesign | Improve OOD trigger calibration |
| Latent-Kept Sequence Pass | 2026-03-29q | Tested decode frequency: per-step vs every-2 vs final-only | LATENT_FINAL_ONLY 82.22% (small n=45); LATENT_KEPT_ADDITIVE 70.37% | Small n for LATENT_FINAL_ONLY; PER_STEP only 57.87% | Substrate prefers latent-kept over tokenizer-like stepwise collapse | Promote to real branch test |
| Latent Verify Branch | 2026-03-29r | Checkpoint-every-3 + low-margin verification trigger | LATENT_VERIFY_DECODE matches PER_STEP_DECODE (72.50%) at 0.492 decode cost | LATENT_DECODE_EVERY3 degrades to 60%; too-sparse decoding hurts | Verification decode is viable; sparse fixed schedule is not | K2 reuse as the operating band |
| Dyno Sweep | 2026-03-29t | Conservative → speculative sweep on latent-kept branch | MODERATE_VERIFY and AGGRESSIVE_SPARSE_K2 both 55% at 0.826 efficiency | AGGRESSIVE_SPARSE_K3 collapses to 34.17% | K3-sparse is the failure mode; K2 is the viable operating region | Formal K2 identification as live band |
| K2 Chain-Length Sweep | 2026-03-29v | Controlled chain depth increase; K2 vs PER_STEP | K2_LATENT_REUSE slightly edges PER_STEP at max_step=12 (63.59% vs 62.82%) | K2 starts weaker at short chains (37.78% vs 51.11% at max_step=2) | K2 accumulates route structure over steps; NOT degrading with depth | Keep chain length as active revisit seam despite positive trend |
| Offset K2/K3 | 2026-03-29w | Fast K2 + slow K3 meta-anchor, various schedules | K2_BASE 50.69% is best | All K3-incorporating variants drop to 34.03% | K3 as co-driver of fast loop hurts regardless of scheduling | K3 doctrine settled to meta/checkpoint duty only |
| K2→K3 Summary | 2026-03-29x | K3 as EMA-style summary lane, NOT controller | K2_BASE, K2_TO_K3_SUMMARY, K2_TO_K3_SUMMARY_FEEDBACK all identical 50.69% | K3 summary adds no benefit (not harmful) | K3 summary is neutral; belongs in colder duties not live loop | Bridge/replay test before revisiting K3 |
| Adaptive K2 Sweep | 2026-03-29y | Margin-driven adaptive collapse frequency | All adaptive variants identical to FIXED_K2 at 50.69% | Margin-only control signal is too weak | Knob class is real; control signal is wrong; not adaptivity disproven | Richer signals: route pressure, carry drift, chain position |
| Multi-Path Latent Benchmark | 2026-03-29z | First direct multi-path route diversity test | PER_STEP_FAMILY 52.08% is best | K2_FAMILY drops to 30.90%; K2_ROUTE_PROBE 24.31% | K2 latent reuse collapses multi-path route diversity | Latent-state probe to distinguish collapse from readout failure |
| Adaptive Multi-Path Rerun | 2026-03-29aa | Added adaptive K2 to multi-path test | Same results: ADAPTIVE_K2 identical to K2 at 32.99% | Route diversity collapse is NOT caused by fixed vs adaptive collapse timing | Readout/projection is now first-class suspect | Route-aware / dual-head readout test |
| Latent State Probe | 2026-03-29ab | Probed whether latent vectors actually preserve family and route identity | K2 stepwise route separability grows monotonically: gap reaches 28.333 at step 6 | Family probe near-chance (46-51%); K2 route behavior probe historically weak | Route structure SURVIVES in latent vectors; readout is flattening it too early | Dual-head readout test; criticality map |
| Latent Criticality Map | 2026-03-29af | Single-dimension ablation on K2 latent vectors | z_YES most critical (total drop 0.0903) | z_MAYBE ablation IMPROVES performance (−0.0312) | z_MAYBE is adding noise; z_YES is load-bearing; distribution relatively uniform across other dims | Dimension-selective readout; drop/gate z_MAYBE |
| Route-Aware Dual-Head Readout | 2026-03-29ae | Separate family head + route head from same latent | FAMILY_ONLY and DUAL_HEAD produce **identical results** (52.08%/41.32%) | Dual-head identical to family-only — implementation may not be structurally distinct | Inconclusive; either implementation error or route info not recoverable via different linear projection | Post-mortem on dual-head implementation; structurally distinct projection needed |

---

## LAYER 4 — DEFNLP-Style Post-Processing Pass
> QA interrogation + catch-what-the-primary-pass-missed scan.

### 4.1 High-Value Facts That Risk Being Orphaned

**F-001: z_MAYBE actively hurts**
The criticality map shows ablating z_MAYBE improves performance (−0.0312 total drop). This is the only dimension with a negative drop score. It has not yet triggered a follow-up test or been logged in the revisit ledger as an active intervention opportunity.

**F-002: K2 route separability is MONOTONICALLY INCREASING over steps 0–6**
The stepwise probe shows K2 route sep gap: 0 → 0.591 → 1.803 → 9.699 → 14.400 → 14.962 → 28.333 → 21.216. This is a dramatic accumulation trajectory, not noise. It directly contradicts any narrative of K2 "collapsing" route information — it's building it. This pattern is not yet named or formally logged as a positive mechanism in the revisit ledger.

**F-003: Dual-head produced identical numbers — needs a code audit flag**
FAMILY_ONLY and DUAL_HEAD results are byte-for-byte identical (52.08 / 41.32 for both). This strongly suggests the two heads aren't structurally distinct. The report logs this as inconclusive but doesn't flag it as a potential implementation defect requiring a specific code-level audit. The revisit ledger should add an explicit "implementation audit required" flag under T-004/T-005.

**F-004: LATENT_FINAL_ONLY reached 82.22% accuracy**
This is the highest family routing accuracy in the corpus on its task, achieved at 0.55 decode cost. Its small N (n=45) correctly warrants caution, but no follow-up with larger N has been scheduled. Given it's the strongest latent-kept result, it should be in the next-step queue.

**F-005: Multi-path K2 drop is more severe in original z than in the rerun**
K2_FAMILY: 30.90% (z) vs 32.99% (aa). Small difference suggesting minor implementation variation between runs. Worth logging as a reproducibility note.

**F-006: OOD UNKNOWN overcommit is 45.83% under FULL_FAM**
This means without the OOD threshold, nearly half of examples are being classified as UNKNOWN. The OOD threshold fixes this to 11.11% but drops accuracy. This overcommit rate is high enough to suggest the family routing itself may be fundamentally uncertain, not just poorly calibrated at the threshold. Not yet logged as a substrate-level concern.

**F-007: REFRESH2_TOP2 preserves 93.9% of FULL_REC accuracy at 57.1% of cost**
This is the best cost-accuracy tradeoff in the recurrent refresh/reuse probe. It hasn't been promoted to a named finding or cross-referenced with the K2 reuse doctrine despite being a direct native parallel.

**F-008: Text encoder is the admitted bottleneck but no encoder redesign has been scheduled**
The nextchar probe sequence (v1→v2→v3→v4→v5) all show the baseline (BASE-0) still winning or tying the best TQ2 runtime. The gap closes with better encoders but never reverses. No formal investigation of why BASE-0 benefits from better representation at the same or higher rate than RB-2R_v3 has been recorded.

### 4.2 Branch Status Summary (Cross-Probe Synthesized)

| Branch / Mechanism | Status | Best Evidence For | Best Evidence Against |
|---|---|---|---|
| RB-2A (whole-plane) | Promoted specialist | 97.12% T1; dominates global motif | Fails T2 (47.12%), T3 (75.53%) |
| RB-2B (blockwise) | Promoted specialist | 100% T2; competitive T3 | Fails T1 (47.12%) |
| RB-2R_v3 (integrated runtime) | Current best runtime | Matches best specialist on T1+T2+T3; edges T4 | T4 only marginally ahead; text accuracy still modest (55.56%) |
| K2 Latent Reuse | Current live band | Chain-length convergence at step 12; stepwise route sep accumulation | Multi-path route diversity collapse (30.90% vs 52.08%); short-chain lag |
| K3 Meta Lane | Demoted to cold-state/audit only | Conceptually sane | Every empirical test with K3 in live loop hurt (34.03%) or was neutral |
| Adaptive K2 | Knob class real; control signal weak | Research literature support; ADAPTIVE_HIGH_COMPRESSION cuts decode cost | No quality improvement over FIXED_K2 on any metric with margin-only signal |
| Latent-Kept Reasoning | Live branch | LATENT_FINAL_ONLY 82.22% (small N); LATENT_VERIFY_DECODE matches PER_STEP at 0.492 cost | Short-chain latent-kept lags per-step; multi-path collapses |
| Recurrent Carry v5 | Current best sequence setup | 30.09% RB-2R_v5_REC vs 20.83% RB-2R_v3_MP; consistent direction across v1→v5 | BASE-0_REC still competes or wins |
| RegimeCache / Refresh-vs-Reuse | Viable; REFRESH2_TOP2 is best ratio | 28.24% at 57.1% cost vs 30.09% at 100% | REFRESH3 degrades significantly |
| OOD Abstention | Reduces overcommit; accuracy tradeoff | UNKNOWN overcommit cut from 45.83% to 11.11% | OOD threshold + reuse combination collapses to 46.30% accuracy |
| Dual-Head Readout | Inconclusive (suspected implementation defect) | Latent-state probe shows route structure exists | Identical results to FAMILY_ONLY — heads may not be distinct |
| Latent Criticality Map | z_YES load-bearing; z_MAYBE adding noise | z_YES highest critical dimension | Distribution relatively flat; weak evidence for strong winning-ticket structure |
| CIL Native Memory | Doctrine-level: adopted | Conceptual coherence with ELT/Exact/Representational split | Not yet instantiated as live test substrate under all branches |

### 4.3 Open Work Queue (All Sources, Consolidated, Priority Ordered)

| Priority | Work Item | Source | Blocking What |
|---|---|---|---|
| 1 | Dual-head readout code audit + structurally distinct re-implementation using stepwise separability gradient | T-004, ae probe, ledger R6 | Route-readout disentangling conclusion |
| 2 | Latent criticality map follow-up: drop/gate z_MAYBE; test dimension-selective projection | Criticality map, F-001 | Readout optimization |
| 3 | LATENT_FINAL_ONLY rerun with larger N | F-004 | Strongest latent-kept finding validation |
| 4 | Route-aware readout re-test on multi-path benchmark specifically | T-001, multi-path failure | K2 multi-path collapse explanation |
| 5 | K3 in multi-path failure regime specifically (not live control — as route-diversity preserver) | A-003, T-003, F-008 | K3 doctrine finalization |
| 6 | Richer adaptive collapse signals: route pressure, carry drift, chain position | A-004, adaptive K2 probe | Adaptive compression knob class |
| 7 | REFRESH2_TOP2 promoted as native RegimeCache reference; cross-reference to K2 reuse doctrine | F-007, recurrent refresh probe | RegimeCache formalization |
| 8 | OOD threshold calibration redesign; investigate overcommit at substrate level | F-006, OOD probe | Abstention reliability |
| 9 | Bridge / hot-cold memory tests | Ledger section 9 | K3 cold-state role; CIL retrieval validation |
| 10 | Text encoder redesign | Z80 probe, nextchar sequence | Text domain viability |
| 11 | Formal CIL ingest of this corpus itself | Extraction gap | CIL doctrine validation |
| 12 | Realistic long-chain tasks (not cycled synthetic sequences) | Chain-length sweep caveat | Live operating band stress test |
| 13 | T5 symbolic sequence + T6 associative recall + T7 teacher distillation | Benchmark harness spec | Benchmark breadth |

---

## Corpus Map
_All 147 files by role_

**Core doctrine / control (7):** TQ2_UNIFIED_ONTOLOGY_v1, CIL_NATIVE_MEMORY_DOCTRINE_v1, RESEARCH_CORPUS_CONSOLIDATION_NOTE, PROCESS_CHECKPOINT_META_EVAL, TQ2_CIL_REVISIT_LEDGER (ac + ad), CONSOLIDATED_NEXT_STEPS (ad), RESEARCH_LAB_INDEX (ad + s), LAB_REVIEW_PACKAGE_MANIFEST

**Architecture specs (3):** TQ2_INTEGRATED_INFERENCE_ARCHITECTURE, TQ2_OBJECT_GRAMMAR, TQ2_BENCHMARK_HARNESS_SPEC

**White papers (versioned, v0.1–v1.0):** WEIGHT_SUBSTRATE_WHITE_PAPER across 10 versions (v0.1_a through v1.0_l)

**Substrate basis docs (versioned):** WEIGHT_SUBSTRATE_BASIS across 14 versions (a through n)

**Substrate index docs:** WEIGHT_SUBSTRATE_INDEX across 9 versions

**Probe spec docs (10):** TQ2_ADAPTIVE_K2_SPEC, TQ2_ADAPTIVE_MULTI_PATH_RERUN_SPEC, TQ2_CHAIN_LENGTH_SWEEP_SPEC, TQ2_DYNO_SWEEP, TQ2_LATENT_KEPT_SEQUENCE_PASS, TQ2_LATENT_STATE_PROBE_SPEC, TQ2_LATENT_VERIFY_BRANCH, TQ2_MULTIPLANE_SEQUENCE_ENCODER_V4, TQ2_RECURRENT_CARRY_ENCODER_V5, TQ2_ROUTE_AWARE_DUAL_HEAD_SPEC, TQ2_LATENT_CRITICALITY_MAP_SPEC, TQ2_MULTI_PATH_LATENT_BENCHMARK_SPEC

**Encoder/architecture notes (5):** TQ2_TEXT_ENCODER_V2, TQ2_TEXT_ENCODER_V3_SEQUENCE, TQ2_RegimeCache_Inspiration_Note, TQ2_calibrated_abstention_note, TQ2_carry_drift_abstention_note, TQ2_family_step_abstention_note, TQ2_ood_recurrence_refresh_note

**Experimental reports (18):** one .md per probe as catalogued above

**Raw data (CSVs + JSONs):** one .csv + one confusions .json per experiment; ~90 raw data files total

**Nested zip:** TQ2_CIL_LAB_REVIEW_PACKAGE_CURRENT_2026-03-29ad.zip (current review package snapshot)

**Hygiene pass:** TQ2_CIL_HYGIENE_PASS_2026-03-29ad
