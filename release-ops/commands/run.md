---
description: Run a release. Drives each step in order, writes results into per-step folders, closes the run when done.
parameters:
  - name: version
    description: Target version (e.g. "0.6.0") or omit for agent proposal based on changes
    required: false
  - name: scope
    description: Which component to release, or omit to be asked
    required: false
---

# Run a release

Read these files before doing anything:

1. This workflow's `index.md` (the manifest, scopes table, run naming scheme).
2. `steps/index.md` (the step map).
3. `runs/example/` (what a correct run looks like, folder by folder).
4. `releases/insights.md` (learned patterns, known issues).
5. `releases/log.md` (past releases, for context on cadence and style).

## Collect parameters

Ask the user for:

- **scope**: which component to release. If `$scope` was passed, confirm it.
- **version**: the target version. If `$version` was passed, confirm it. If omitted, propose one after step 1 (collect) based on the changes.

## Create the run folder

Name the run folder `<scope>-v<version>` (e.g. `myapp-v0.6.0`). If version is not yet known, create the folder after step 1 when you propose it.

Create `runs/<run-name>/index.md` with:

- The run scope and version.
- A per-step status table with every step from `steps/index.md`, all marked pending.

Create `runs/<run-name>/0-parameters.md` with the scope, version, and any other inputs.

## Execute each step

For each step in `steps/index.md`, in order:

1. Read the step file (e.g. `steps/0-preflight.md`).
2. Execute it as described.
3. Create a folder in the run named like the step file without the extension (e.g. `0-preflight/`).
4. Write the step's output to `results.md` (or the format the step specifies) inside that folder. If the step generates a script, save it next to the results.
5. Update the run's `index.md`: mark the step as done in the status table.

If a step says to skip (e.g. no registry configured), still create its folder with a `results.md` that says "Skipped" and why.

If a step fails, stop. Write the failure into the step's `results.md`, mark it as failed in the status table, and report to the user. Do not continue to the next step.

If a step pauses for user approval (e.g. step 3, version bump), present the proposal and wait. Only proceed after explicit confirmation.

## Close the run

When all steps are done:

1. Create `done/info.md` with: what was released, the version, a one-paragraph summary, and anything learned that should update the steps or insights.
2. Update the run's `index.md` to mark the run as done.
3. If the run surfaced a new insight (a blocker, a flaky check, a better procedure), append it to `releases/insights.md`.
