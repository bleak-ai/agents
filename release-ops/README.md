# Release Ops

A release agent that collects changes, drafts a changelog, bumps the version, publishes, and optionally announces. Each release is a searchable run. The agent learns your changelog style and known blockers over time.

## Install

```
gcontext add release-ops
```

## How it works

1. Ask for a release, with or without a target version.
2. The agent gathers the changes and drafts the changelog.
3. You approve the version bump.
4. It tags, publishes, and checks the deploy.
5. Release notes go out where you chose.

## Connections

- `source-control`: the git host where the repository lives (GitHub, GitLab, or similar).
- `package-registry` (optional): the registry to publish to (PyPI, npm, crates.io, or similar).
- `deploy-target` (optional): the platform that auto-deploys on push (Coolify, Vercel, Netlify, or similar).
- `notification-sink` (optional): where to post release announcements (Slack, Discord, email, or similar).

## What it learns

Your changelog style, known blockers and workarounds, and a searchable history of every release.

## Layout

- `commands/`: user-invokable entry points.
- `runs/`: one folder per release.
- `steps/`: the release flow, from preflight to announce.

See `index.md` for the full agent definition.
