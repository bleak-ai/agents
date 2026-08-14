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
3. If the user picks a new dedicated instance, create it: start Chrome detached with its own `--user-data-dir` (a folder outside the agent state, e.g. `~/.browser-cookbook/chrome`) and a free debug port.
4. Record the roster in the browser connection's `index.md`: one line per known instance (name, debug port, user-data-dir or "daily profile", what it is for, logged-in sites as they accumulate) and which one is DEFAULT. Every run attaches to the default unless the user names another instance for that run; a recipe may pin an instance in its own index.md.

## 2. Verify the connection

Never ask the user about environment state a probe can answer; check it, and fix it yourself when you can.

1. Probe the chosen instance's port. If it answers, note the Chrome version and continue.
2. If the probe fails, start or restart that instance yourself with its recorded flags. Say one line first: "Restarting Chrome with the debug port; your tabs restore." For the daily profile: quit Chrome gracefully first (macOS: `osascript -e 'tell application "Google Chrome" to quit'`), wait until the process is gone, then start detached with `open -a "Google Chrome" --args --remote-debugging-port=<port>` (plus the recorded `--user-data-dir` for a dedicated instance). Probe again.
3. Only if that restart fails, or the platform is not macOS, give the user the one exact command to run.
4. Smoke-test the attachment with an ad-hoc script: connect Playwright over CDP to the recorded port, read the title of the active tab, and report it. Read the browser connection's `index.md` for the exact snippet.
5. If Playwright is missing from the connection deps, add it to the connection's `connection.yaml`. Then tell the user: "Restart the server (stop, `gcontext up`), then reconnect in your client (`/mcp` in Claude Code)."

## 3. Explain the knowledge layout

Tell the user, in plain words: the agent keeps notes per site in `sites/` and saved recipes in `recipes/`; both start empty and fill through use. Point at the example run as a sample.

One client tip: register this MCP server under a short alias (for example `bc`); commands then read `/mcp__bc__browse`. Command names are short (no module prefix, except names the framework reserves, like this setup command, which keeps the module prefix), so with a short alias every daily command, including per-recipe ones, stays easy to find in the picker. In Claude Code: `claude mcp remove <long-name>` then `claude mcp add <short-name> --transport http <url>`.

## What setup creates

- The instance roster with a default, recorded in the browser connection.
- A verified browser connection.
- Nothing else. Site knowledge and recipes are created during use.
