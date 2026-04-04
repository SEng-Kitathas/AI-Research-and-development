# Weight Substrate — Research Crosswalk
_Version: 2026-03-28a_

## Purpose
This crosswalk translates the current project shape into research seams and evidence status.

Confidence values below indicate how strongly the literature supports the direction **for this project stage**.

---

## S-01 — Balanced ternary / low-bit state spaces
**Project claim:** low-bit or ternary-friendly discrete states are a valid native substrate direction.

**Confidence:** 90%

**Why it matters**
- supports ternary base states
- supports cheap arithmetic
- supports compact storage and edge-friendly execution

**Research support**
- Tong et al. 2024 — balanced symmetry ternary CIM hardware
- Zhu et al. 2022 — unified ternary/binary/mixed-precision inference with efficient representation
- Di Guglielmo et al. 2020 — binary/ternary FPGA deployment with large resource savings

**Architectural implication**
The project is justified in keeping ternary or ternary-friendly nativity as a substrate invariant.

---

## S-02 — Integer-only / low-bit arithmetic as a serious path
**Project claim:** useful training/inference can live in constrained arithmetic regimes.

**Confidence:** 84%

**Research support**
- Wang et al. 2020 (NITI) — integer-only training framework
- Zhong et al. 2020 — low-bit training with scaling schemes
- Shawahna et al. 2022 (FxP-QNet) — mixed low-precision fixed-point deployment

**Architectural implication**
Cheap closed math is not an aesthetic choice; it is a defensible research direction.

---

## S-03 — Sparse additive ternary arithmetic
**Project claim:** ternary systems can exploit sparsity and addition-friendly execution.

**Confidence:** 86%

**Research support**
- Zhu et al. 2022 (FAT) — ternary weight networks replacing multiplications with additions and exploiting zero-skipping
- Zhu et al. 2022 (TAB) — efficient ternary pipelines and storage formats

**Architectural implication**
Whole-object or blockwise ternary transforms deserve serious evaluation, especially if they preserve additive closure.

---

## S-04 — Quaternion / grouped structured representations
**Project claim:** grouped/hypercomplex representations can model relations more efficiently than flat scalar-only formats.

**Confidence:** 85%

**Research support**
- Qin et al. 2022 — fast quaternion product units
- Altamirano-Gómez & Gershenson 2023 — quaternion CNN review
- Chen et al. 2021 — quaternion factorization machines

**Architectural implication**
RB-1 remains a legitimate baseline branch rather than dead ancestry.

---

## S-05 — Spectral companion transforms
**Project claim:** a spectral companion layer is plausible if it remains a lift of the base algebra.

**Confidence:** 80%

**Research support**
- Duong-Ngoc et al. 2023 — efficient NTT architecture
- Li et al. 2022 — compact/efficient NTT accelerator
- Waris et al. 2025 — pipelined NTT for Kyber

**Architectural implication**
Loop-B / spectral branch is real enough to keep, but should be exact-transform-first, not mystical-scheduler-first.

---

## S-06 — Knowledge distillation / weight consumption
**Project claim:** standard models/weights can be consumed and distilled into a native smaller substrate.

**Confidence:** 82%

**Research support**
- Cantini et al. 2024 — distillation of large language models to lighter students
- Zhang et al. 2021 — self-distillation
- Shawahna et al. 2022 — post-training self-distillation in quantization

**Architectural implication**
RB-5 is real enough to keep as a formal branch.
The napkin “consume standard weights / distill content” line is directionally validated.

---

## S-07 — Salience / sparsity / active-inference control layer
**Project claim:** salience-driven sparse organization and self-organizing control are directionally coherent.

**Confidence:** 72%

**Research support**
- Friston et al. 2022 — sparse coupling and self-organization under FEP
- Parr & Friston 2018 — generalized free energy and active inference
- Raja et al. 2021 — important critique against overextending FEP

**Architectural implication**
The control lineage remains alive, but FEP should be treated as a bounded formal seam, not a universal solvent.

---

## S-08 — Reversible / adiabatic computing
**Project claim:** reversibility matters, but hardware and software claims must be separated.

**Confidence:** 92% for hardware seam, 25% for current software-path strong claim

**Research support**
- Takeuchi et al. 2017 — reversibility and adiabatic superconductor logic
- Frank & Shukla 2021 — foundations of classical reversible computing
- Hong et al. 2016 — experimental test of Landauer principle

**Architectural implication**
Keep reversible computing in the crosswalk as a hardware seam only.
Do not treat end-to-end software reversibility as established.

---

## S-09 — Scheduler / update law experimentation
**Project claim:** update law matters and should be treated as a branch family.

**Confidence:** 72% for annealing/Metropolis-type ideas; 15% for zeta as privileged schedule

**Research support**
- Kuo et al. 2022 — simulated annealing for network structure optimization
- Polowczyk et al. 2025 — simulated annealing hybrid optimization in GCNs

**Architectural implication**
Metropolis/annealing belongs in RB-7.
Zeta timing remains experimental-only unless it earns evidence.

---

## S-10 — Napkin genealogy: plane/block/radical grammar
**Project claim:** the project has an ancestral line based on plane/block decomposition, radical assignment, and geometric permutation.

**Confidence:** 88% as internal genealogy, 38% as externally validated specific formalism

**Evidence chain**
- Napkin extraction pass
- TQ2/Tesseract shadow decision
- explicit user clarification: combinatory space, whole-object vs blockwise transforms, cheap math, 4D mutagenic lift

**Architectural implication**
RB-2 should be written as a formal object grammar, not just as prose about “Tesseract.”

---

## Summary
The evidence currently supports:
- branch-based exploration over a shared substrate
- TQ2 as current build-favored branch
- TQ1 as valid baseline
- spectral and distillation branches as live
- scheduler/reversibility claims only when bounded and tested

The evidence does not currently support:
- strong zeta privilege
- blanket software reversibility
- treating a single branch as already proven truth
