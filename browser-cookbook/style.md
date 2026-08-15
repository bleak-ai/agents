# Message style

Every command and step follows these rules. They override any default verbosity.

## Module-relative paths

All paths in this module are relative to the module folder. When this module is installed under `modules/`, prefix every path with `modules/browser-cookbook/`. For example: `recipes/index.md` becomes `modules/browser-cookbook/recipes/index.md`. This rule applies to every `read_file`, `write_file`, `run_script`, and `list_dir` call.

## Status lines

One line per action, format `LABEL: detail`. Fixed vocabulary, nothing else:

ANALYZING, EXPLORING, BROWSING, TESTING, SAVING, RUNNING, HEALING, BLOCKED, FAILED, DONE

- Print a status line when a phase starts or the action changes, not for every micro-step.
- No prose between status lines. Do not announce what you are about to do; the label already says it.
- Prose is allowed at exactly three points: a proposal the user must approve, a blocker, and the final result.
- The final result is the data (table, list, value), then DONE, then at most one follow-up line.

## Questions

- Every enumerable choice goes through the client's structured question tool
  (AskUserQuestion in Claude Code): proposal approval, run selection, blocker
  resolution, setup choices.
- Free text only for genuinely open answers. When you offer drafted wording,
  the user must always be able to supply their own.
- If the client has no structured question tool, ask in chat with numbered options.

## Printed commands

- Never print a slash command you have not constructed. The alias is the
  `name` field in `gcontext.yaml` at the state root; read it with
  `read_file("gcontext.yaml")`. The real invocation is
  `/mcp__<alias>__<command>`.
- Fallback: when your tool names carry a prefix (`mcp__<alias>__read_file`),
  that prefix is the alias and confirms the value. Behind a proxy client the
  prefix is absent or rewritten; trust `gcontext.yaml` and tell the user the
  command may appear under a different prefix in their client's picker.
- Example: alias `bc` gives `/mcp__bc__save_recipe` and
  `/mcp__bc__recipe_gmail_check`.

## Run folders

- Every run folder is `runs/<YYYY-MM-DD>-<slug>/` (today's date, then the
  two-or-three-word kebab slug from step 0).
- At the start of any command that touches `runs/`, delete run folders older
  than 7 days that have no `done/` marker. Successful `browse` runs count:
  only promotion (save_recipe) or the recipe flow writes `done/`. Use an
  ad-hoc script; the tool set has no delete. One SAVING line reports how many
  were removed, none if zero. Never delete a run named in the current
  command's arguments. Age comes from the date in the folder name; skip
  folders whose name does not match the pattern.

## Blockers

On a blocker (captcha, unexpected 2FA, unexpected wall): print BLOCKED with
what is needed, ask through the question tool (solved, continue / abort), and
message the notification connection if one exists. A notification connection
is any `connections/<name>/` with kind `notification-sink` in its
`connection.yaml`. The user acts in the visible Chrome window; verify the
page state, then continue.
