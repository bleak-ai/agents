# Message style

Every command and step follows these rules. They override any default verbosity.

## Module-relative paths

All paths in this module are relative to the module folder. When this
module is installed under `modules/`, prefix every path with
`modules/diagram-crafter/`. This rule applies to every `read_file`,
`write_file`, `run_script`, and `list_dir` call.

## Status lines

One line per action, format `LABEL: detail`. Fixed vocabulary, nothing else:

LOADING, SCOPING, WIREFRAMING, DRAFTING, RENDERING, SAVING, BLOCKED, FAILED, DONE

- Print a status line when a phase starts or the action changes, not for
  every micro-step.
- No prose between status lines. Do not announce what you are about to do;
  the label already says it.
- Prose is allowed at exactly three points: a proposal the user must
  approve, a blocker, and the final result.
- The final result is the path to the saved SVG, then DONE, then at most
  one follow-up line.

## Questions

- Every enumerable choice goes through the client's structured question
  tool (AskUserQuestion in Claude Code): wireframe selection, composition
  change confirmation, save confirmation, scoping questions with
  enumerable answers.
- Free text only for genuinely open answers (the initial text, label
  wording corrections).
- If the client has no structured question tool, ask in chat with numbered
  options.

## Decision split

- Composition (which archetype, which panels, order, connections, what is
  included, label wording) belongs to the user. Every composition decision
  goes through the question tool.
- Style (color, typography, spacing, icons, arrows) belongs to `design/`
  and is never negotiated per run. If the user pushes back on a style
  point, apply the correction to the current diagram, and when the same
  correction happens a second time, propose writing it into the relevant
  `design/` file through the question tool (write / keep one-off).

## Printed commands

- Never print a slash command you have not constructed. The alias is the
  `name` field in `gcontext.yaml` at the state root; read it with
  `read_file("gcontext.yaml")`. The real invocation is
  `/mcp__<alias>__<command>`.
- Fallback: when your tool names carry a prefix (`mcp__<alias>__read_file`),
  that prefix is the alias and confirms the value. Behind a proxy client
  the prefix is absent or rewritten; trust `gcontext.yaml` and tell the
  user the command may appear under a different prefix in their client's
  picker.

## Run folders

- Every run folder is `runs/<YYYY-MM-DD>-<slug>/` (today's date, then a
  two-or-three-word kebab-case slug derived from the task).
- At the start of any command that touches `runs/`, delete run folders
  older than 7 days that have no `done/` marker. Use an ad-hoc script; the
  tool set has no delete. One SAVING line reports how many were removed,
  none if zero. Never delete a run named in the current command's
  arguments. Age comes from the date in the folder name; skip folders
  whose name does not match the pattern.

## Rendering

- Rendering through `scripts/render.py` is best effort. If it reports
  NO_BROWSER or fails for any reason, continue without it and do not
  mention the failure to the user beyond a single RENDERING line saying
  the check was skipped. Never treat a render failure as a blocker.

## Blockers

On a blocker (source text missing or too thin to scope, contradictory
scoping answers): print BLOCKED with what is needed, ask through the
question tool (solved / abort), and message the notification connection if
one exists. A notification connection is any `connections/<name>/` with
kind `notification-sink` in its `connection.yaml`.
