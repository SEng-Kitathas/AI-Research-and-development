# KarnOS/SYNAPSE/Yggdrasil — Shadow Maintenance Note
_Version: 2026-03-27a_

---

## CURRENT ACTIVE SEAMS (ranked by build pressure)

1. **S17 (Tesseract Geometric Inference)** — HIGHEST. The weight architecture decision is made. Spec must be rewritten from TQ2 ground truth.
2. **S16 (KSL-Ω Static Analysis Engine)** — HIGH. Standard Library macros are drafted. Implementation closes the "safety without overhead" gap.
3. **S14 (Wave Equation)** — HIGH. Law 10 replaces diffusion with wave physics. FDTD stencil same cost. Needs Architect validation.
4. **S9 (Metropolis Criterion)** — HIGH. Strictly better training algorithm. One comparison per weight update.
5. **S1 (FEP/Active Inference)** — MEDIUM. Theoretical foundation proven. Needs documentation, not implementation.
6. **S12 (Fractal Escalation)** — MEDIUM. Powers-of-3 hierarchy defined. Thresholds need empirical calibration.

## UPDATE RULES

### When to update the Trace Matrix
- A requirement is added, removed, or changed scope
- An implementation status changes (Missing→Partial→Implemented)
- An OD is resolved
- Build order changes
- A new subsystem is identified

### When to update the Research Crosswalk
- A new research seam is identified
- An existing seam's confidence level changes
- A seam's architectural implication changes
- A cross-link between seams is discovered
- External validation confirms or denies a seam

### When to update the Addendum
- After every major work session that produces findings
- When a design law emerges from discourse
- When the Architect makes a normative decision (like "Tesseract is the weight style")

### When to update this Maintenance Note
- When active seams change priority
- When the update discipline itself needs revision
- When new rules emerge

## ORDERING RULES

1. **Matrix before Crosswalk** — requirements drive research, not the other way around
2. **Addendum before Matrix** — capture fresh insight before formalizing
3. **Never update the spec without updating the Matrix** — the shadow layer must track all spec changes
4. **Never resolve an OD without documenting the source** — every resolution must cite its evidence chain

## PRESERVATION RULES

1. Shadow docs are NEVER deleted — only superseded by dated successors
2. The Addendum captures DELTAS, not full state — it compresses, doesn't duplicate
3. The Crosswalk captures SEAMS, not individual papers — research translates to build pressure
4. The Matrix captures TRUTH, not aspiration — "Partial" is honest, "Implemented" requires evidence

## CURRENT DOCUMENT SET

| Document | Path | Lines | Updated |
|---|---|---|---|
| Trace Matrix | KarnOS-Shadow-Trace-Matrix-2026-03-27a.md | ~150 | 2026-03-27 |
| Research Crosswalk | KarnOS-Shadow-Research-Crosswalk-2026-03-27a.md | ~170 | 2026-03-27 |
| Addendum | KarnOS-Shadow-Addendum-2026-03-27a.md | ~60 | 2026-03-27 |
| Maintenance Note | KarnOS-Shadow-Maintenance-Note-2026-03-27a.md | this file | 2026-03-27 |
| OD Resolution Candidates | OD_RESOLUTION_CANDIDATES.md | ~500 | 2026-03-27 |
| Full Forensic Extraction | FULL_FORENSIC_EXTRACTION_ALL_PROJECTS.md | ~300 | 2026-03-22 |
| Tesseract Corpus Synthesis | TESSERACT_CORPUS_FORENSIC_SYNTHESIS.md | ~300 | 2026-03-27 |
| GODSPEC v3.1.0 (current spec) | GODSPEC_v3.1.0.md | ~6,233 | 2026-03-22 |
| GODSPEC v4.0.0 TENTATIVE | GODSPEC_v4_0_0_TENTATIVE.md | ~900 | 2026-03-27 (uploaded) |

## WHAT "READY FOR FINAL SPEC" LOOKS LIKE

- [ ] Architect validates Laws 7-14 (individually, not as a block)
- [ ] Tesseract (TQ2) replaces TQ1 throughout the spec
- [ ] KSL-Ω Standard Library macros implemented and tested in FASM
- [ ] ODs 47, 51, 53, 54, 55 formally resolved with evidence chains
- [ ] Wave equation (Law 10) decision made (wave vs diffusion vs NS)
- [ ] Loop B (NTT spectral inference) parameters finalized (OD-58)
- [ ] All 4 implementation patches from v4 tentative applied
- [ ] Seed Crystal build order documented as step-by-step
- [ ] QA spine: what tests exist for each subsystem?
- [ ] First build attempted: `fasm src/main.asm karnos.efi` → QEMU

## THE SINGLE RULE

**If the shadow layer stops updating, the project is drifting.**
If you're doing work and the Matrix doesn't change, either the work didn't matter or you forgot to record it.

## LESSONS FROM THIS SESSION (2026-03-22 through 2026-03-27)

1. **Read ALL corpus BEFORE editing spec.** This session applied TQ1 to v3.1.0 then discovered TQ2 in the Tesseract corpus. The TQ1 edits are now ancestral. Law 0 demands discourse before implementation — that includes reading before writing.

2. **Search for shapes, not terms.** `grep 'ternary'` finds ternary references. It does NOT find the Cardinal 5-layer architecture that is isomorphic to KarnOS's 5-layer architecture. Structural pattern matching requires asking "what is this thing's shape?" not "does this mention the keyword?"

3. **Context compaction is inevitable.** This 5-day thread compacted multiple times. Workspace files survive compaction. Context window content does not. Always write findings to files IMMEDIATELY, not at the end of a reasoning chain.

4. **The shadow layer should start at session start, not session end.** This session created the shadow docs at the end. They should have been created at the beginning and updated incrementally. Next session: load shadow docs first, update as you go, emit final versions at end.

5. **Every external AI evaluation (Gemini, GPT, Perplexity) is a research seam.** The Gemini KSL-Ω enforcement evaluation is S16 in the Crosswalk. The GPT 8-iteration evaluation was S-GPT-EVAL (partially processed). These are not "opinions" — they are adversarial audits that either confirm or challenge the architecture. Treat them as data, not commentary.

6. **Workspace files survive compaction. Always check first.** This session's workspace at `/home/claude/` contains: `karnos/` (Seed Crystal skeleton with src/, include/, build/, impls/), `GODSPEC_v3.1.0.md` (339KB working spec), `karnos_seed_crystal.tar.gz`, `neal_corpus/` (NEAL zip extracts), `ksl_omega.inc` published to outputs. On context loss, these files ARE the project state.

7. **The transcript at `/mnt/transcripts/` is raw JSON of every tool call.** 9 transcripts from this project span 10,000+ lines. They are the forensic recovery tool if shadow docs are somehow lost. Read incrementally — never try to load the whole transcript at once.

---

_Process mirrors PROBE→DERIVE→EMBODY→RECURSE. The shadow layer IS the project's memory._

