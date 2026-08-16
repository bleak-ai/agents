---
description: Verify archetype and design seeds, report render availability.
---

Read this agent's `index.md` first.

Follow `style.md` for questions and printed commands; setup is
conversational, the status-line vocabulary does not apply here.

## 1. Verify seeds

Purpose: confirm the module shipped complete.

1. Check that `archetypes/` contains `index.md` and the six seed files:
   pipeline-flow, layered-stack, before-after, cycle-loop, timeline,
   concept-hero. Report any missing.
2. Check that `design/` contains `index.md`, `palette.md`,
   `typography.md`, `layout.md`, and `icons.md`. Report any missing.
3. Check that `diagrams/index.md` exists. If missing, create it with a
   title line and a "(no diagrams yet)" note.

## 2. Probe rendering

Purpose: learn whether best-effort self-review will work here.

Run `scripts/render.py` with `run_script` and the single argument
`--check`. Report one line: render available with the browser path, or
render unavailable so self-review will be skipped. Either result is
fine; unavailable is not an error.

## 3. Explain the layout

Purpose: orient the user before the first craft run.

Tell the user, in plain words: `archetypes/` holds the diagram shapes,
`design/` is the fixed style, `diagrams/` fills with finished work.
Point at the example run as a sample. List the six archetypes with
their one-line summaries.
