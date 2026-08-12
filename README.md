# gcontext agent registry

This repo is the public registry of agent templates for [gcontext](https://github.com/bleak-ai/gcontext).
Each top-level folder is one agent. The folder name is the agent id.

## Install an agent

```
gcontext add <agent-id>
```

For example: `gcontext add release-ops`

Any public GitHub repo subfolder also works:

```
gcontext add https://github.com/yourorg/yourrepo/tree/main/my-agent
```

## Available agents

| Id | Description |
|----|-------------|
| `browser-cookbook` | Learn your sites, crystallize repetitive browser tasks into scripts that self-heal |
| `release-ops` | Collect changes, draft a changelog, bump the version, publish, and announce |
| `seo-pipeline` | Research keywords and build a prioritized list of content ideas |
| `support-ops` | Resolve tickets, log actions, and build playbooks from experience |

## Submit an agent

Open a PR that adds exactly one new folder.

Requirements:

- The folder must pass `gcontext share <folder>` validation locally.
- The `runs/` directory must contain only the fabricated example run with invented data (no real names, emails, or credentials).
- Do not edit `registry.json`. Maintainers regenerate it with the build script in the gcontext repo after merge.

A maintainer reviews and merges.

## Agent spec

See the full agent specification: <https://github.com/bleak-ai/gcontext/blob/main/docs/agents.md>
