# Diagram Crafter

Turn a text into a polished explanatory diagram, hand-crafted as SVG. The
agent asks what single claim the diagram must make, shows 2-3 ASCII
wireframe options built from proven diagram archetypes, and expands the one
you pick using a written design system. You decide composition; the design
system keeps style consistent across runs.

## Install

```
gcontext add diagram-crafter
```

Then run setup:

```
/mcp__<instance>__diagram_crafter__setup
```

## How it works

1. You paste the initial text and name the audience.
2. Scoping: one round of questions (max 4) pins down the single claim, what
   the reader must compare or follow, and what to leave out.
3. Wireframe: the agent picks 2-3 candidate archetypes and draws one small
   ASCII wireframe per candidate with the real labels from your text. You
   pick one or ask for a mix. Wireframes fix composition only.
4. Draft: the agent expands the wireframe into an SVG using the archetype
   skeleton and the design system, and saves it to the run folder.
5. Review: if a headless Chrome is available locally, the agent screenshots
   the draft and self-checks it before showing it. If not, you get the file
   directly. Rendering is an aid, never a required step.
6. Feedback: you react, the agent edits the file. Composition changes go
   back through a one-line wireframe confirmation.
7. The final SVG lands in `diagrams/` with a metadata header.

## Archetypes

Six seed archetypes, each an editable markdown file in `archetypes/`:

- `pipeline-flow` - actors and hops, left to right.
- `layered-stack` - what sits on what.
- `before-after` - two states, the difference highlighted.
- `cycle-loop` - a repeating process.
- `timeline` - stages over time.
- `concept-hero` - one idea, one big visual metaphor.

## What it learns

- `diagrams/`: every finished SVG, tagged with archetype, claim, source
  summary, and date. The wireframe step consults it to reuse compositions
  that worked.
- `design/`: the design system itself. When you correct a style decision
  twice, the agent proposes writing it into the relevant design file.

## Requirements

None. SVG output renders in any browser. The optional self-review step uses
a locally installed Chrome or Chromium when it finds one, and silently
skips otherwise.

## Layout

- `commands/`: user-invokable entry points.
- `steps/`: the five-step flow (intake, wireframe, draft, review, save).
- `archetypes/`: diagram shapes with wireframe templates and SVG skeletons.
- `design/`: palette, typography, layout rules, icon library.
- `diagrams/`: finished diagrams.
- `runs/`: one folder per execution.
- `scripts/`: the render script for best-effort self-review.
- `style.md`: the message regime every command follows.

See `index.md` for the full agent definition.
