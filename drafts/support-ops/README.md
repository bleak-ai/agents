# Support Ops

A support agent that resolves tickets, logs every action, and builds playbooks from experience. Each resolved ticket becomes a searchable record. Repeated patterns become reusable playbooks the agent consults on future tickets.

## Install

```
gcontext add support-ops
```

## How it works

1. Hand the agent a ticket, or say `next` to pull the top of the queue.
2. Approve the plan it proposes.
3. Watch it execute, approving each write action.
4. It logs the run and closes the ticket.
5. Recurring patterns become playbooks it reuses on future tickets.

## Connections

- `ticket-tracker`: the issue tracker where support tickets live (Linear, Jira, GitHub Issues, or similar).
- `product-api`: the product's own API or database, for executing fixes.

## What it learns

Playbooks from recurring ticket patterns, and a searchable history of every ticket it resolves.

## Layout

- `commands/`: user-invokable entry points.
- `playbooks/`: reusable resolutions built from experience.
- `runs/`: one folder per resolved ticket.
- `steps/`: the resolution flow.

See `index.md` for the full agent definition.
