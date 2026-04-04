# Weight Shadow Addendum
_Pass: 2026-03-29c_

## New decision

**Whole-plane, blockwise, and hybrid are likely not separate runtime answers.**
They are likely the cooperating mechanics of one TQ2 inference engine.

## Why this changed

The substrate probe did not produce a universal winner.
It produced task-shaped winners.

That means:
- global geometry matters sometimes
- local composition matters sometimes
- a real substrate should preserve both

## New doctrine

- Separate them to measure them
- Compose them to run them

## Immediate consequences

1. Canonical runtime becomes:
   `blockwise -> whole-plane -> hybrid reconciliation`
2. Benchmark harness must report:
   - isolate scores
   - integrated runtime score
3. Forge must ultimately optimize for:
   - local motif compatibility
   - global geometric compatibility

## Updated phrasing worth preserving

**"The substrate is one thing. The branches are how we measure it. The integrated stack is how it likely works."**
