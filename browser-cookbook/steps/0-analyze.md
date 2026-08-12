# Step 0: Analyze the task

## Purpose

Understand the task, find what is already known, define success.

## Input

The task description; `recipes/index.md`; `sites/<domain>/` if present.

## Output

- `runs/{slug}/index.md`: target, goal, and a status line.
- `runs/{slug}/0-analysis/results.md` with:
  - **Target**: URL or app.
  - **Goal**: one sentence.
  - **Success definition**: how to verify it worked (a file exists, a value changed, n items found).
  - **Read-only or mutating**: does the task change anything on the site?
  - **What we already know**: matching recipe (name), site notes present or absent, relevant blocks.

## How to execute

1. Parse the task. If the target is unclear, ask the user.
2. Derive the kebab-case slug for the run folder.
3. Create `runs/{slug}/index.md` with the target, the goal, and a status line. Keep the status updated as steps complete.
4. Check `recipes/index.md` for a matching recipe. If one matches, tell the user and suggest `run_recipe`. Stop here if they agree.
5. Read `sites/<domain>/index.md` if it exists. Note which blocks and lib helpers apply.
6. Write the analysis file and present it briefly.

## Done when

The analysis file is written and the user has confirmed the goal and success definition.
