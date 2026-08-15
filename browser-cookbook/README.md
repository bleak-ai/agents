# Browser Cookbook

A browser agent that learns your sites. It performs browser tasks through your real Chrome, so your logins persist. It accumulates per-site knowledge and crystallizes repetitive tasks into plain Python scripts. On later runs the AI only dispatches the script and heals failures. Blockers like captchas escalate to you.

## Install

```
gcontext add browser-cookbook
```

## How it works

1. Describe a browser task in plain words.
2. The agent reuses a saved recipe when one matches.
3. Known sites run warm from accumulated site notes.
4. `browse` performs without saving a recipe; `new_recipe` crystallizes one; `save_recipe` promotes the last browse run into a recipe.
5. Broken recipes diagnose and heal themselves (3 attempts, then report).

Each saved recipe also becomes its own slash command (`recipe_<name>`), so you can invoke it straight from the client's command picker.

## Connections

- `browser`: Playwright attached over CDP to a Chrome instance you choose (your daily profile or a dedicated one).

## What it learns

Two layers. `sites/<domain>/` holds how each site works (map, reusable blocks, a Python helper lib) and grows on every browser contact, even failed ones. `recipes/<name>/` holds per-task recipes; a script is the default outcome, and skipping it needs a written justification.

## Layout

- `commands/`: user-invokable entry points.
- `sites/`: per-site knowledge, one folder per domain.
- `recipes/`: one folder per crystallized task.
- `runs/`: one folder per execution.
- `steps/`: the four-step flow (analyze, explore, propose, test).
- `style.md`: the message regime every command follows.

See `index.md` for the full agent definition.
