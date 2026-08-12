---
description: Set up browser-cookbook. Verifies the Chrome debug connection and explains the knowledge layout.
---

Read this agent's `index.md` and `steps/index.md` first.

## 1. Verify the browser connection

The agent needs Chrome running with a debug port and your normal profile.

1. Ask the user to start Chrome with remote debugging if it is not already running that way. The command on macOS:
   `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
   (An already-running Chrome without the flag must be quit first.)
2. Smoke-test the attachment with an ad-hoc script: connect Playwright over CDP to `http://127.0.0.1:9222`, read the title of the active tab, and report it. Read the browser connection's `index.md` for the exact snippet.
3. If Playwright is missing from the connection deps, add it to the connection's `connection.yaml`. Then tell the user: "Restart the server (stop, `gcontext up`), then reconnect in your client (`/mcp` in Claude Code)."

## 2. Explain the knowledge layout

Tell the user, in plain words: the agent keeps notes per site in `sites/` and saved recipes in `recipes/`; both start empty and fill through use. Point at the example run as a sample.

## What setup creates

- A verified browser connection.
- Nothing else. Site knowledge and recipes are created during use.
