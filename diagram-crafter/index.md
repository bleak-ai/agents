---
id: diagram-crafter
name: Diagram Crafter
description: >
  A diagram agent that turns an initial text into a polished explanatory
  visual, hand-crafted as SVG. It scopes the single claim the diagram must
  make, proposes 2-3 ASCII wireframe compositions built from proven
  archetypes, and expands the chosen one using a written design system so
  results stay consistent across runs. The user decides composition; the
  design system decides style. Finished diagrams accumulate in a library
  the agent consults on later runs.
flow:
  - Paste the initial text and name the audience
  - Scoping questions pin down the single claim, what the reader must compare or follow, and what to leave out (one round, max 4)
  - The agent picks 2-3 candidate archetypes and shows one small ASCII wireframe per candidate with real labels; the user picks one or asks for a mix
  - The agent expands the wireframe into an SVG draft using the archetype skeleton and the design system
  - Best effort self-review, when a headless browser is available the agent screenshots and checks the draft before showing it
  - Feedback loop, the user reacts and the agent edits the file; composition changes go back through a one-line wireframe confirmation
  - Final SVG saved to diagrams/ with a metadata header
connections: []
tags: [diagrams, visuals, communication]
learns: >
  diagrams/ holds every finished SVG with a metadata header (archetype,
  claim, source summary, date), so the wireframe step can reuse
  compositions that worked and avoid repeating weak ones. design/ is the
  editable design system: when the user corrects a style decision twice,
  the agent proposes writing the correction into the relevant design file.
---

# Diagram Crafter

Create explanatory diagrams as hand-crafted SVG: the agent scopes the
claim, the user picks an ASCII wireframe composition, and the design
system fixes the style so runs stay consistent. All paths here are
relative to this module folder; after `gcontext add`, prefix them with
`modules/diagram-crafter/`.

- `commands/`: entry points; `craft.md` creates a diagram from a text (the
  main command), `setup.md` verifies seeds and reports render availability.
- `steps/`: the ordered five-step flow the craft command follows.
- `archetypes/`: one file per diagram shape, with its scoping questions,
  an ASCII wireframe template, and a skeleton SVG.
- `design/`: the written design system (palette, typography, layout,
  icons); style is never negotiated per run.
- `diagrams/`: finished SVGs, each with a metadata header; the library
  later runs consult.
- `runs/`: one folder per execution, named by date and task slug.
- `scripts/`: `render.py`, the best-effort screenshot for self-review.
- `style.md`: the message regime every command follows.
