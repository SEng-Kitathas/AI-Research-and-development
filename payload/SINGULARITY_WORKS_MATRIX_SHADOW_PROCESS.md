# Singularity Works — Matrix & Shadow Docs Process
_Last updated: 2026-03-27T12:35:00Z_

## Purpose

This process exists to stop complex projects from dissolving into:
- chat drift
- duplicated ideas
- forgotten requirements
- disconnected research
- untracked changes
- fake progress

It creates a **persistent operational memory** for a project by maintaining a small set of live documents that:
1. preserve requirements,
2. preserve research,
3. preserve implementation state,
4. preserve deltas over time,
5. preserve the chain from idea → evidence → build.

This is not just “note taking.”
It is a **control system for long-horizon project work**.

---

## The Core Idea

Treat the conversation, uploaded artifacts, research findings, and code/build state as inputs into a **living trace system**.

The system is made of:
1. a **Trace Matrix**
2. a **Research Crosswalk**
3. an **Addendum**
4. a **Maintenance Note**
5. optional support files like:
   - CSV exports
   - specs
   - schemas
   - HUD/operator docs
   - enforcement docs

Together, these form the project’s **shadow documentation layer**.

“Shadow” means:
- always running alongside the build
- always lag-minimizing
- always preserving continuity
- always available to restore context after long threads, tool resets, or design pivots

---

## The Document Set

## 1. Trace Matrix
This is the master operational table.

It records:
- requirements
- desired subsystems
- research-backed refinements
- implementation status
- build priority
- notes on what is real vs partial vs missing

### What goes in it
Each row should have:
- `id`
- `requirement`
- `status`
- `notes`

### Recommended status values
- **Implemented**
- **Partial**
- **Missing**

### What the matrix is for
Use it to answer:
- What are we actually trying to build?
- What exists already?
- What is still missing?
- What just got promoted from idea to requirement?
- What should be built next?

---

## 2. Research Crosswalk
This is the compounding-research document.

It records:
- major research seams
- what each seam contributes
- how seams reinforce each other
- what architectural changes those seams justify

### What goes in it
For each seam:
- seam name
- representative papers / sources
- key takeaway
- architectural implication
- cross-links to other seams

### What the crosswalk is for
Use it to answer:
- What does the external research actually validate?
- Which ideas are supported, weak, or only speculative?
- Where do different disciplines converge on the same structure?
- What refinement vectors are worth promoting into the build?

---

## 3. Addendum
This is the quick-delta compression note.

It records:
- the newest meaningful findings
- newly promoted design rules
- fresh architectural consequences
- new “laws” or phrasing worth preserving

### What goes in it
- a short list of new high-value findings
- the new practical consequences
- short laws or design principles that fell out of the latest pass

### What the addendum is for
Use it to answer:
- What changed in this most recent pass?
- What did we learn that is worth carrying forward immediately?
- What changed in how we should think about the project?

---

## 4. Maintenance Note
This is the discipline document.

It records:
- how the shadow docs should be maintained
- what counts as a required update
- what the current active seams are
- what the operator should do after each major change

### What goes in it
- update rules
- ordering rules
- current active high-priority seams
- preservation rules

### What the maintenance note is for
Use it to answer:
- How do we keep this system alive?
- When do we update which doc?
- What discipline prevents the shadow layer from decaying?

---

## Optional Support Files

These are created when needed:
- CSV export of matrix
- subsystem specs
- schemas
- HUD/operator docs
- enforcement specs
- runtime flow docs
- final architecture drafts
- implementation plans

These are not the core control loop, but they are generated from it.

---

## The Operating Cycle

This is the default workflow.

## Phase 1 — Ingest
Collect inputs from:
- current thread
- prior thread context
- uploaded files
- generated artifacts
- research pulls
- code/build state

Do not treat any one source as sufficient by itself.

---

## Phase 2 — Diff
Compare new information against the current shadow layer.

Ask:
- Is this a new requirement?
- Is this a refinement of an old requirement?
- Is this a status change?
- Is this a new research seam?
- Is this a new subsystem?
- Is this a correction to something already recorded?

Do not overwrite blindly.
Prefer **delta-aware updates**.

---

## Phase 3 — Promote
Only promote items into the matrix/crosswalk if they are one of the following:
- directly requested by the operator
- validated by repeated thread emphasis
- supported by research
- required to make another subsystem coherent
- clearly load-bearing for the build

This prevents the docs from becoming a junk drawer.

---

## Phase 4 — Update the Trace Matrix
When something affects:
- requirement scope
- implementation status
- build ordering
- subsystem priority
- architecture status

update the matrix.

### Promotion rule
A concept moves into the matrix when it becomes one of:
- a real subsystem
- a real requirement
- a real implementation dependency
- a real build-order consideration

---

## Phase 5 — Update the Research Crosswalk
When external research changes how the system should be designed:
- add the seam
- summarize its contribution
- note how it compounds with existing seams
- note what it justifies architecturally

Do not just list papers.
Translate research into build pressure.

---

## Phase 6 — Update the Addendum
When there is a meaningful new pass:
- summarize the highest-value findings
- capture new design laws
- note immediate consequences

This is the fastest way to preserve fresh insight before it diffuses.

---

## Phase 7 — Update the Maintenance Note
When the discipline itself changes:
- add the new rule
- revise the active seams
- revise the update expectations

This is how the process avoids rotting.

---

## Phase 8 — Emit Build-Grade Specs
When enough seams converge:
- turn shadow knowledge into subsystem specs
- turn subsystem specs into schemas
- turn schemas into implementation planning docs
- turn planning docs into build skeletons

The shadow layer feeds spec generation.
Spec generation feeds implementation.

---

## Phase 9 — Recurse
Repeat after:
- every major requirement change
- every meaningful research pass
- every subsystem spec
- every build milestone
- every major implementation delta

This is a recursive process, not a one-time planning exercise.

---

## The Process as a State Machine

The clean state machine is:

1. **Observe**
2. **Classify**
3. **Diff**
4. **Promote**
5. **Record**
6. **Cross-link**
7. **Order**
8. **Spec**
9. **Build**
10. **Audit**
11. **Repeat**

This mirrors the broader project law:
**PROBE → DERIVE → EMBODY → RECURSE**

The shadow-doc system is the project-memory version of that loop.

---

## How to Use This in Practice

## Every session
At the start of a meaningful work session:
1. load the latest matrix
2. load the latest crosswalk
3. load the latest addendum
4. load the latest maintenance note
5. identify current active seams
6. decide whether the session is:
   - research
   - consolidation
   - spec
   - build
   - audit

## After each major change
Update:
- matrix if requirements/status/order changed
- crosswalk if research changed design
- addendum if fresh findings matter
- maintenance note if process discipline changed

## Before implementation
Check:
- does the matrix reflect the real build order?
- do the specs exist?
- are the research-backed refinements already promoted?
- is the QA/evidence spine represented, not just the feature spine?

## After implementation
Record:
- implemented vs partial vs missing
- evidence/gate state
- new risks
- simplification opportunities
- new residuals

---

## Naming Convention

Use dated rolling files where useful, plus stable “current” names if desired.

Suggested pattern:
- `Project-Shadow-Trace-Matrix-YYYY-MM-DDx.md`
- `Project-Shadow-Trace-Matrix-YYYY-MM-DDx.csv`
- `Project-Shadow-Research-Crosswalk-YYYY-MM-DDx.md`
- `Project-Shadow-Research-Addendum-YYYY-MM-DDx.md`
- `Project-Shadow-Maintenance-Note-YYYY-MM-DDx.md`

Support docs:
- `PROJECT_SUBSYSTEM_SPEC.md`
- `PROJECT_SCHEMA.json`
- `PROJECT_FINAL_ARCHITECTURE_DRAFT.md`

The point is:
- preserve chronology
- preserve update lineage
- avoid ambiguity about which revision is newer

---

## Promotion Rules

A finding should be promoted into the shadow layer when it is:
- repeated
- load-bearing
- architecture-shaping
- research-validated
- implementation-relevant
- or process-critical

A finding should stay out when it is:
- decorative
- speculative with no build consequence
- redundant with an existing row/seam
- not yet differentiated from mere preference

---

## Research Rules

When doing research:
- group findings by seam, not by paper
- prefer representative papers over giant citation dumps
- record what the seam changes in the build
- record what other seams it reinforces
- record uncertainty honestly

Do not treat research as trivia collection.

The crosswalk exists to transform research into architecture.

---

## QA Rules

The shadow layer must always track both:
1. the **feature/build spine**
2. the **QA/evidence spine**

If one advances without the other, the project drifts.

This is mandatory.

The matrix should eventually capture:
- feature requirements
- recovery requirements
- QA gate requirements
- traceability requirements
- assurance requirements
- operator/HUD requirements

---

## Residual-Risk Rules

Never hide uncertainty.

If something is:
- partial
- residual
- speculative
- not yet wired
- not yet validated

say so in the matrix or supporting specs.

This preserves trust and prevents false closure.

---

## When You Are “Ready for Final Spec”

You are ready when:
- the matrix is stable enough that build order is clear
- the crosswalk has promoted the major research seams
- the main subsystem specs exist
- the QA/evidence spine is represented
- the orchestration flow is defined
- the traceability/assurance chain is defined
- operator-surface/HUD requirements are defined if needed

At that point, stop widening and consolidate.

---

## The Core Laws of the Process

### Law 1 — No orphan insight
If a finding matters, it must land in the shadow layer or a spec.

### Law 2 — No fake progress
A long discussion does not count as advancement unless the shadow layer or specs move.

### Law 3 — No silent overwrite
Update by diff, not by amnesia.

### Law 4 — No disconnected research
Research must end in a build implication or stay out.

### Law 5 — No feature-only planning
The QA/evidence spine must advance with the feature spine.

### Law 6 — No context loss
The shadow layer exists to survive thread length, tool resets, and long project duration.

### Law 7 — No unjustified complexity
If complexity survives, it should do so with a recorded reason.

### Law 8 — No evidence debris
Evidence should roll into claims, risks, or assurance—not remain a loose pile.

---

## Minimal Reusable Template

You can reuse this exact workflow on any serious project:

1. Create a trace matrix
2. Create a research crosswalk
3. Create an addendum
4. Create a maintenance note
5. Update them after every meaningful research/spec/build delta
6. Emit specs only after the shadow docs stabilize
7. Build only after the spec chain is coherent
8. Audit and recurse

---

## Short Version

The matrix/shadow-doc process is:

> a persistent project-memory and control system
> that converts conversation, research, artifacts, and implementation state
> into a live traceable structure for planning, verification, and build sequencing.

It is how you keep a complex project from dissolving into chat history.

