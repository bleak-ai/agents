# Step 1: Wireframe

## Purpose

Fix the composition before any SVG exists. This step always runs, even
when the user names an archetype in the task.

## Input

`0-intake/results.md`; `archetypes/` (all files); `diagrams/index.md`.

## Output

- `runs/{date}-{slug}/1-wireframe/results.md` with every candidate
  wireframe, the reasoning lines, and the user's choice.

## How to execute

1. Read `archetypes/index.md` and match the claim shape from intake to
   2-3 candidate archetypes. If the user named an archetype, it is
   candidate one; still bring 1-2 alternatives.
2. For each candidate, read its archetype file and draw one small ASCII
   wireframe from its template, using the REAL labels from the intake
   text, never placeholders. Add exactly one line of reasoning per
   candidate: why this shape serves the claim.
3. Wireframes fix composition only: panels, order, connections, what is
   included, label wording. Do not mention color, icons, or typography;
   those belong to `design/` and are not options.
4. Present the candidates through the question tool: one option per
   wireframe (label = archetype name plus the reasoning line), plus the
   built-in Other for a mix or a change. WIREFRAMING status line first,
   the wireframes themselves are the proposal prose allowed by
   `style.md`.
5. If the user asks for a mix or edits, redraw the single merged
   wireframe and confirm it through the question tool (approve /
   adjust). Loop until approved.
6. Write the results file with all candidates and the approved
   wireframe marked.
7. Set the run index status line to `wireframe approved`.

## Done when

Exactly one wireframe is approved and recorded.
