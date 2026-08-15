---
id: browser-cookbook
name: Browser Cookbook
description: >
  A browser agent that learns your sites. It performs browser tasks through
  your real Chrome, accumulates per-site knowledge, and crystallizes
  repetitive tasks into plain Python scripts; on later runs the AI only
  dispatches the script and heals failures. Broken
  knowledge heals itself; blockers like captchas escalate to you.
flow:
  - Describe a browser task in plain words
  - The agent reuses a saved recipe when one matches
  - Known sites run warm from accumulated site notes
  - browse performs without saving a recipe; new_recipe crystallizes one
  - Broken recipes diagnose and heal themselves (3 attempts, then report)
connections:
  - kind: browser
    description: Playwright attached over CDP to a Chrome instance the user chooses (daily profile or a dedicated one; roster with a default recorded in the connection)
    examples: [Chrome CDP via Playwright]
tags: [automation, browser]
learns: >
  Two layers. sites/<domain>/ holds how each site works (map, reusable
  blocks, a Python helper lib) and grows on every browser contact, even
  failed ones. recipes/<name>/ holds per-task recipes; a script is the
  default outcome and skipping it needs a written justification.
---

All paths in commands and steps are relative to this module folder. After `gcontext add`, prefix each path with `modules/browser-cookbook/` (see `style.md` for the full rule).

Turn browser work into accumulated knowledge. The agent drives your real Chrome (your logins persist), records what it learns about each site, and turns repetitive tasks into parameterized Python scripts that replay in seconds; the AI only launches the script and steps in when it breaks.

Token economy is a design goal: AI time is spent only where judgment is needed. Deterministic parts (login, navigation, extraction) live in per-site Python helpers even when the task itself stays AI-driven.

## Entry points

- `browse`: do the task, no recipe. Site knowledge still updates.
- `new_recipe`: do the task and crystallize a recipe (full explore, verdict, save flow).
- `save_recipe`: promote the last browse run into a recipe, no re-exploration.
- `run_recipe`: execute a saved recipe by name; heals itself on failure.
- `recipe_<name>`: one slash command per saved recipe, generated from the `recipe.md` template (hyphens in the recipe name become underscores). Pick it straight from the client's command picker; same execution and healing as `run_recipe`.

## The script verdict

After every `new_recipe` exploration the agent writes a verdict into the recipe: script candidate or not, with the reason. The default is yes; NOT scripting must be justified (content-dependent branching, layout instability, anti-bot pressure). The verdict includes an anchoring block that names each element anchor and its strategy (text-label, aria-role, stable-id, or css-class) with an overall durability rating. On success, a per-site `selftest.py` is written or updated to assert every recorded anchor still resolves.

## Blockers

Captcha, unexpected 2FA, strange modal: the agent pauses and asks in the session. If a notification connection exists (e.g. Telegram), it also sends a message there. You fix it in the visible Chrome window; the run continues from the same page.

## Run naming

Each run folder is named with a kebab-case slug derived from the task description, decided during step 0 (analyze).

## Contents

- `commands/`: user-invokable entry points (browse, new_recipe, save_recipe, run_recipe, recipe template, setup).
- `sites/`: per-site knowledge, one folder per domain, shared by every recipe and run.
- `recipes/`: one folder per crystallized task, with goal, verdict, and script.
- `runs/`: one folder per execution, named by task slug.
- `steps/`: the four-step flow (analyze, explore, propose, test).
