---
id: release-ops
name: Release Ops
description: >
  A release agent that collects changes, drafts a changelog, bumps the
  version, publishes, and optionally announces. Each release is a searchable
  run; the agent learns your changelog style and known blockers over time.
parameters:
  - name: version
    description: Target version (e.g. "0.5.0"). Omit it and the agent proposes one from the collected changes.
    required: false
  - name: scope
    description: Limit to a specific package in a monorepo (e.g. "@acme/core")
    required: false
flow:
  - Ask for a release, with or without a target version
  - The agent gathers the changes and drafts the changelog
  - Approve the version bump
  - It tags, publishes, and checks the deploy
  - Release notes go out where you chose
connections:
  - kind: source-control
    description: The git host where the repository lives (GitHub, GitLab, or similar)
    examples: [GitHub, GitLab, Bitbucket]
  - kind: package-registry
    description: The registry to publish to (PyPI, npm, crates.io, or similar). Optional; skip if the project has no published package.
    examples: [PyPI, npm, crates.io]
  - kind: deploy-target
    description: The platform that auto-deploys on push (Coolify, Vercel, Netlify, or similar). Optional; skip verify-deploy if not configured.
    examples: [Coolify, Vercel, Netlify]
  - kind: notification-sink
    description: Where to post release announcements (Slack, Discord, email, or similar). Optional; skip if not needed.
    examples: [Slack, Discord, Microsoft Teams]
tags: [release, ops, devtools]
learns: >
  This agent records your changelog style, known blockers, and workarounds,
  and keeps a searchable history of every release.
---

Ship a release with a repeatable seven-step procedure. Each run takes one release from preflight to announcement, logs the result, and feeds learnings back into future runs.

The `version` parameter accepts an explicit semver string (e.g. "1.2.0") or can be omitted. When omitted, the agent proposes major/minor/patch based on the changes collected in step 1. The agent always asks for confirmation before applying a version bump.

The `scope` parameter is for monorepos. When set, the agent limits change collection, version bumping, and publishing to the named package. When omitted, the agent operates on the entire repository.

Run folders are named by version: `v{version}` (e.g. `v0.5.0`). If a second release happens the same day with the same version prefix, append `-b` (e.g. `v0.5.0-b`).

## How it learns

The agent accumulates knowledge in two ways:

1. **Release history** (`releases/log.md`): a table of every release with scope, version, date, summary, and notes. The agent consults it to understand release cadence and past decisions.

2. **Insights** (`releases/insights.md`): created during setup. Records the repo's changelog style (tone, grouping, detail level), known-flaky checks, common blockers, and workarounds. The agent consults this during preflight and changelog drafting.

## Files

- [index.md](index.md) - this file, agent entry point
- [steps/index.md](steps/index.md) - the seven release steps (0-preflight through 6-announce)
- [commands/](commands/) - user-invokable slash commands (setup, run)
- [runs/](runs/) - one folder per release run
- [releases/log.md](releases/log.md) - release history table
- [releases/insights.md](releases/insights.md) - learned patterns and known issues
