# Project Continuation Protocol (Generic)
_Version: 2026-03-29ax_

## Purpose
This protocol makes restart deterministic:
**upload archive > continue**

## Recommended archive contents
- rehydration note
- SOP
- current state / next steps
- doctrine snapshot
- extraction docs
- key reports
- manifest + checksums

## Recommended resume command
“Read the archive in load order, rehydrate the project state, state incumbent baseline vs open seams, then continue from the current-state / next-steps file.”

## Archive discipline
- keep manifests
- keep checksums
- prefer additive updates
- do not silently replace older doctrine/state files
- include an index if the archive is nontrivial
