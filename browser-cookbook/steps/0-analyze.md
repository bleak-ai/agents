# Step 0: Analyze the task

## Purpose

Understand the task, find what is already known, define success.

## Input

The task description; `recipes/index.md`; `sites/<domain>/` if present.

## Output

- `runs/{date}-{slug}/index.md`: target, goal, and a status line.
- `runs/{date}-{slug}/0-analysis/results.md` with:
  - **Target**: URL or app.
  - **Goal**: one sentence.
  - **Success definition**: how to verify it worked (a file exists, a value changed, n items found).
  - **Read-only or mutating**: does the task change anything on the site?
  - **What we already know**: matching recipe (name), site notes present or absent, relevant blocks.

## How to execute

1. Parse the task. If the target is unclear, ask the user.
2. Derive the kebab-case slug (two or three short words: it becomes the recipe name and its slash command). The run folder is `runs/<YYYY-MM-DD>-<slug>/` per `style.md`.
3. Check `recipes/index.md` for a matching recipe. If one matches, offer it through the question tool (run the recipe / continue). Running it means: read `commands/run_recipe.md` and follow it, skipping its lookup step. Stop here if they agree.
4. Create `runs/{date}-{slug}/index.md` with the target, the goal, and a status line. Keep the status updated as steps complete. This happens only when no matching recipe was accepted.
5. Read `sites/<domain>/index.md` if it exists. Note which blocks and lib helpers apply.
6. Write the analysis file. Present target, goal, success definition as three short lines; confirm through the question tool (correct / adjust). This confirmation gate exists because a recipe is a durable artifact; flows that save nothing must not use it.

## Done when

The analysis file is written and the user has confirmed the goal and success definition.
