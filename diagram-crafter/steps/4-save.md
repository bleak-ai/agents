# Step 4: Save

## Purpose

Store the approved diagram in the library with the metadata that makes
it findable and reusable.

## Input

The approved SVG; `0-intake/results.md`; `1-wireframe/results.md`.

## Output

- `diagrams/<slug>.svg`: the final file with a metadata header.
- A new line in `diagrams/index.md`.
- `runs/{date}-{slug}/done/info.md`.

## How to execute

1. Prepend the metadata header to the SVG as a comment block directly
   after the XML/root opening, exactly this shape:

   ```xml
   <!-- diagram-crafter
   archetype: <archetype id>
   claim: <the claim sentence>
   source: <one-line summary of the initial text>
   audience: <who it was made for>
   date: <YYYY-MM-DD>
   notes: <optional: what was hard, what the user corrected>
   -->
   ```

2. Save as `diagrams/<slug>.svg` (the run slug; on collision append
   `-2`, `-3`).
3. Append one line to `diagrams/index.md`:
   `` - `<slug>.svg`: <archetype>; <claim sentence> ``
4. Write `runs/{date}-{slug}/done/info.md` with the final path and date.
5. Print the final result per `style.md`: the saved path, DONE, and at
   most one follow-up line.

## Done when

The SVG with header is in `diagrams/`, the index has its line, and the
run has its `done/` marker.
