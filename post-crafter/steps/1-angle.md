# Step 1: Angle

## Purpose

Decide the single claim or story this post makes. The product info is
stable per product; the angle is what makes this post different from the
last one.
Without it, every post converges on the differentiator list.

## Input

- `runs/{date}-{slug}/0-intake/results.md` (product, goal, segment, past
  posts with their angles).
- `products/<product-slug>/info.md`.

## Output

- `runs/{date}-{slug}/1-angle/results.md` with:
  - **Proposed angles**: 3-5 candidates, each with its reasoning.
  - **Chosen angle**: the one the user picked (or wrote), one sentence.

## How to execute

1. Read the past-posts list from intake. Note which angles, formulas, and
   levers are already used for this product.
2. Propose 3 to 5 distinct angles. An angle is one sentence stating the
   single claim or story of the post. Draw from these types:
   - **Personal story**: a real frustration and what it led to.
   - **Contrast against a known alternative**: from the positioning section
     of `info.md`.
   - **Concrete use case**: one task, shown end to end.
   - **Counterintuitive claim**: a belief the audience holds, challenged.
   - **Transformation**: a concrete before and after.
3. For each proposed angle show:
   - The claim (one sentence).
   - Why it fits the goal and the chosen segment (one sentence).
   - Nearest past post, if any, and how this angle differs.
4. Never propose an angle that repeats a past post's angle for this
   product.
5. Present through the question tool. The user picks one or writes their
   own.
6. Write the results file. Set the run index status line to `angle chosen`.

## Done when

The user has chosen the angle and the results file is written.
