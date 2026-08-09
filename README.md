# gcontext workflow registry

This repo is the public registry of workflow templates for [gcontext](https://github.com/bleak-ai/gcontext).
Each top-level folder is one template. The folder name is the template id.

## Install a template

```
gcontext add <id>
```

For example: `gcontext add release-ops`

Any public GitHub repo subfolder also works:

```
gcontext add https://github.com/yourorg/yourrepo/tree/main/my-template
```

## Available templates

| Id | Description |
|----|-------------|
| `browser-recipes` | Explore browser actions with AI, then crystallize them into reusable scripts |
| `release-ops` | Collect changes, draft a changelog, bump the version, publish, and announce |
| `seo-pipeline` | Research keywords and build a prioritized list of content ideas |
| `support-ops` | Resolve tickets, log actions, and build playbooks from experience |

## Submit a template

Open a PR that adds exactly one new folder.

Requirements:

- The folder must pass `gcontext share <folder>` validation locally.
- The `runs/` directory must contain only the fabricated example run with invented data (no real names, emails, or credentials).

A maintainer reviews and merges.

## Template spec

See the full template specification: <https://github.com/bleak-ai/gcontext/blob/main/docs/workflows.md>
