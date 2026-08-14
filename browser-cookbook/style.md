# Message style

Every command and step follows these rules. They override any default verbosity.

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

- Never print a slash command you have not constructed. The server alias is
  client-side; derive it from your own MCP tool names: the tools are named
  `mcp__<alias>__read_file` and so on, so the real invocation is
  `/mcp__<alias>__<command>`.
- Example: alias `bc` gives `/mcp__bc__save_recipe` and `/mcp__bc__recipe_gmail_check`.

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
message the notification connection if one exists. The user acts in the
visible Chrome window; verify the page state, then continue.
