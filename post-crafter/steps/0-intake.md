# Step 0: Intake

## Purpose

Load the product knowledge, pick the audience segment, and define what this
post should achieve. Ask only what `products/<product-slug>/info.md` does not
already answer.

## Input

The task description; `products/` (state root); `posts/` folder.

## Output

- `runs/{date}-{slug}/index.md`: product, goal, segment, and a status line.
- `runs/{date}-{slug}/0-intake/results.md` with:
  - **Product**: which product this post is for.
  - **Goal**: what the post should achieve (awareness, launch, feature
    highlight, social proof, other).
  - **Segment**: the one audience segment this post targets, with its
    awareness stage.
  - **Key differentiator**: the one differentiator this post leans on.
  - **Past posts**: for each previous post about this product, its angle,
    headline formula, and persuasion levers (from `posts/` frontmatter).

## How to execute

1. Parse the task description. Identify the product name.
2. Derive the kebab-case slug (two or three words). The run folder is
   `runs/<YYYY-MM-DD>-<slug>/` per `style.md`.
3. Read `products/index.md` (state root). Load `products/<product-slug>/info.md`.
4. If no `info.md` exists, create it from the template in
   `commands/setup.md`, asking the user through the question tool for:
   - What the product does (one sentence).
   - Who it is for, as one or more segments (one line each).
   - What problem it solves (one sentence).
   - What makes it different from alternatives (list).
   - Known alternatives and where each falls short (for positioning).
   - Any real numbers (users, downloads, time saved). "none yet" is valid.
   Register the product in `products/index.md`.
5. If `info.md` exists, do not re-ask anything it already answers. Only ask
   about missing or clearly stale fields.
6. Present the segments from `info.md` through the question tool. The user
   picks the one this post targets.
7. If the chosen segment has no awareness stage recorded, ask once through
   the question tool (unaware / problem aware / solution aware / product
   aware) and save it to `info.md`. Reuse it in every later run.
8. Ask the user to confirm or adjust the goal through the question tool.
   Check the "Post defaults" section of `info.md` first and propose the
   default goal if one is recorded.
9. Scan `posts/` for previous posts about this product. Read each file's
   frontmatter and list angle, headline_formula, and persuasion_levers in
   the results file.
10. Pick the one differentiator from `info.md` that best serves the goal
    and the chosen segment. Propose it in the results file; the user can
    override it during confirmation.
11. Write the intake results file. Present product, goal, segment as three
    short lines. Confirm through the question tool (correct / adjust).
12. Set the run index status line to `intake done`.
13. Write any new or corrected answers back to `info.md`.

## Done when

The intake file is written, the user has confirmed product, segment, and
goal, and `info.md` reflects everything learned.
