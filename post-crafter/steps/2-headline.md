# Step 2: Headline workshop

## Purpose

Generate headline candidates that serve the chosen angle, score them, attack
the best ones, and let the user pick from the survivors. This is the most
important step. Spend the most resources here.

## Input

- `runs/{date}-{slug}/1-angle/results.md` (chosen angle).
- `runs/{date}-{slug}/0-intake/results.md` (goal, segment, awareness stage).
- `formulas/` folder (all formula files).
- `products/<product-slug>/info.md`.
- `voice.md`.

## Output

- `runs/{date}-{slug}/2-headline/results.md` with:
  - **Candidates**: every generated candidate with formula and scores.
  - **Red team**: the top 5 with the strongest objection each.
  - **Selected headline**: the one the user picked (or wrote).
  - **Variations**: 2-3 refinements of the selected headline.
  - **Final headline**: the one that goes into the post.

## How to execute

### Phase A: generate wide

1. Read every file in `formulas/`. Filter out formulas that do not fit:
   - Wrong awareness stage for the chosen segment (each formula file states
     its stage fit).
   - Missing raw material: skip number-anchor and social-proof when
     `info.md` has no real numbers; skip scarcity when nothing is truly
     scarce.
2. Generate 15 to 25 candidates. Every candidate serves the chosen angle,
   not the whole product info. Multiple candidates per formula are allowed
   and expected for the strong formulas.

### Phase B: score

3. Score every candidate 1 to 5 on each criterion, then sum (max 25):
   - **Specificity**: could only this product say it.
   - **Front-load**: the benefit or tension lands in the first six words.
   - **Provable**: every claim in it is true and demonstrable today.
   - **Angle fit**: it serves the chosen angle, not a different one.
   - **Voice fit**: it passes `voice.md` and the product voice notes.

### Phase C: red team

4. Take the top 5 by total score. For each, write the most likely
   dismissive comment from a skeptical technical reader (one or two
   sentences, in the reader's voice).
5. If a headline does not survive its objection, revise it once or drop it
   and promote the next candidate by score.

### Selection

6. Present only the surviving top 5 through the question tool: headline,
   formula, total score, strongest objection, and whether it survives. The
   user picks one or writes their own.
7. Generate 2-3 variations of the selection:
   - One shorter (tighter, punchier).
   - One that shifts the frame (loss to gain, "you" to "I").
   - One that adds a specific detail from `info.md`.
8. Present variations through the question tool. The user picks the final
   headline.
9. Write the results file with the full scored candidate list (all of
   them, not only the top 5), the red team notes, the selection, and the
   final headline. Set the run index status line to `headline chosen`.

## Headline quality rules

- Specific beats generic. "Save 2 hours/week" beats "Save time".
- Numbers anchor, but only real ones. No invented metrics.
- Identity signals ("developers who...") create instant relevance.
- The headline must be true. No false scarcity, no fake authority.
- If the user would be uncomfortable saying it out loud, dial it back.

## Done when

The user has selected the final headline and the results file is written.
