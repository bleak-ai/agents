---
description: Set up browser-cookbook. Verifies the Chrome debug connection and explains the knowledge layout.
---

Read this agent's `index.md` and `steps/index.md` first.

## 1. Verify the browser connection

The agent needs Chrome running with a debug port and the user's normal profile. Never ask the user about environment state a probe can answer; check it, and fix it yourself when you can.

1. Probe the port with an ad-hoc script: HTTP GET `http://127.0.0.1:9222/json/version`. If it answers, note the Chrome version and continue to the smoke test.
2. If the probe fails, restart Chrome with the flag yourself. Say one line first: "Restarting Chrome with the debug port; your tabs restore." Then run an ad-hoc script that quits Chrome gracefully (macOS: `osascript -e 'tell application "Google Chrome" to quit'`), waits until the process is gone, starts it detached with `open -a "Google Chrome" --args --remote-debugging-port=9222`, and probes again.
3. Only if that restart fails, or the platform is not macOS, give the user the one exact command to run. On macOS:
   `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
   (An already-running Chrome without the flag must be quit first.)
4. Smoke-test the attachment with an ad-hoc script: connect Playwright over CDP to `http://127.0.0.1:9222`, read the title of the active tab, and report it. Read the browser connection's `index.md` for the exact snippet.
5. If Playwright is missing from the connection deps, add it to the connection's `connection.yaml`. Then tell the user: "Restart the server (stop, `gcontext up`), then reconnect in your client (`/mcp` in Claude Code)."

## 2. Explain the knowledge layout

Tell the user, in plain words: the agent keeps notes per site in `sites/` and saved recipes in `recipes/`; both start empty and fill through use. Point at the example run as a sample.

## What setup creates

- A verified browser connection.
- Nothing else. Site knowledge and recipes are created during use.
