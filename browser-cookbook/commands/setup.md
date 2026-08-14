---
description: Set up browser-cookbook. Chooses the Chrome instance the agent uses, verifies the debug connection, and explains the knowledge layout.
---

Read this agent's `index.md` and `steps/index.md` first.

Follow `style.md` for questions and printed commands; setup is conversational, the status-line vocabulary does not apply here.

## 1. Choose the browser instance

The agent drives Chrome over a debug port. A machine can run several Chrome instances (different profiles or user-data-dirs). The user decides which one the agent uses by default; a run can name a different one when needed.

1. Discover candidates with an ad-hoc script: probe ports 9222-9225 with HTTP GET `/json/version`, and list running Chrome processes with their `--user-data-dir` and `--remote-debugging-port` flags.
2. Ask ONE question through the client's structured question tool: which instance should the agent use by default? Offer the discovered instances plus "a new dedicated one". State the consequences inside the options, plainly:
   - Daily profile: logins already exist, but the agent acts under the user's own accounts, the debug port lets any local process drive that logged-in browser, and the window is busy while the agent works.
   - Dedicated instance: the user keeps working in their own Chrome in parallel and the exposure is limited to that instance, but each site needs one manual login the first time.

   The binary for a dedicated instance depends on the OS:
   - macOS: use Chrome Beta when it is installed (a separate app bundle, so Dock and Raycast clicks do not land in the automation window). When Beta is absent, plain Chrome with its own `--user-data-dir` works; do not require an install.
   - Linux and Windows: plain Chrome with its own `--user-data-dir`. On Windows the taskbar behavior is unverified; watch for the same hijack symptom (clicks on the pinned icon landing in the automation window) and note it in the roster if it appears.
3. If the user picks a new dedicated instance, create it yourself with one ad-hoc script; the user picks nothing manually. The script: choose the binary per the OS rule above, create the `--user-data-dir` (a folder outside the agent state, e.g. `~/.browser-cookbook/chrome`), find a free debug port, launch the browser detached and headed (never headless; blockers need a visible window), poll `GET /json/version` on the port until it answers, then report name, port, data dir, binary, and Chrome version.
4. Record the roster in the browser connection's `index.md`: one line per known instance (name, debug port, user-data-dir or "daily profile", binary or bundle, what it is for, logged-in sites as they accumulate) and which one is DEFAULT. Every run attaches to the default unless the user names another instance for that run; a recipe may pin an instance in its own index.md.

## 2. Verify the connection

Never ask the user about environment state a probe can answer; check it, and fix it yourself when you can.

1. Probe the chosen instance's port. If it answers, note the Chrome version and continue.
2. If the probe fails, start or restart that instance yourself with its recorded flags. Say one line first: "Restarting Chrome with the debug port; your tabs restore." For the daily profile: quit Chrome gracefully first (macOS: `osascript -e 'tell application "Google Chrome" to quit'`), wait until the process is gone, then start detached with `open -a "Google Chrome" --args --remote-debugging-port=<port>` (plus the recorded `--user-data-dir` for a dedicated instance). Probe again.
3. Only if that restart fails, or the platform is not macOS, give the user the one exact command to run.
4. Smoke-test the attachment with an ad-hoc script: connect Playwright over CDP to the recorded port, read the title of the active tab, and report it. Read the browser connection's `index.md` for the exact snippet.
5. If Playwright is missing from the connection deps, add it to the connection's `connection.yaml`. Then tell the user: "Restart the server (stop, `gcontext up`), then reconnect in your client (`/mcp` in Claude Code)."

## 3. Explain the knowledge layout

Tell the user, in plain words: the agent keeps notes per site in `sites/` and saved recipes in `recipes/`; both start empty and fill through use. Point at the example run as a sample.

## 4. Finish

Print this template verbatim as the last message, with the alias derived per `style.md` and the real instance name, Chrome version, and port filled in. Nothing after it.

```
Setup complete. Default instance: <name> (Chrome <version>, port <port>).

Commands, in the order to try them:
1. /mcp__<alias>__browse - one-off browser task. Try: /mcp__<alias>__browse task: check my starred GitHub repos
2. /mcp__<alias>__new_recipe - do a task and save it as a reusable recipe. Try it when a task repeats.
3. /mcp__<alias>__save_recipe - promote the last browse run into a recipe, no re-exploration.
4. /mcp__<alias>__run_recipe - run a saved recipe by name (each saved recipe also gets its own /mcp__<alias>__recipe_<name> command).

Start with 1.
```

## What setup creates

- The instance roster with a default, recorded in the browser connection.
- A verified browser connection.
- Nothing else. Site knowledge and recipes are created during use.
