---
description: Set up support-ops for your team. Maps your ticket tracker and product connections, creates the playbook structure, and verifies access.
---

Read this agent's `index.md` and `steps/index.md` first to understand what support-ops does and what it needs.

## 1. Map the product connections

Ask the user which systems their support team operates on. These are the services where fixes happen: a database, a payment provider, an admin API, etc. There can be one or many.

For each service, find the matching connection in the agent's environment. Record each one with its read/write permission level.

## 2. Fill the integration mapping

`playbooks/_index.md` holds the integration mapping: how the generic playbook references map to the user's specific connections. For each connection mapped in the previous step, write one line explaining which playbook references (e.g. "the payment provider") map to which connection.

The two example playbooks (`example-swap-subscription.md` and `example-export-member-list.md`) ship with the template. Leave them in place as format references.

## 3. Smoke test

Run a dry intake on one real ticket:

1. Query the tracker for the most recent ticket.
2. Fetch its details.
3. Identify the customer (or confirm the product connection can look them up).
4. Present the intake summary.

Do not change any ticket status or write to the product systems. This is read-only.

## What setup creates

- The integration mapping in `playbooks/_index.md`.
- Nothing else. The example playbooks and the runs/example/ folder ship with the template. Real runs and real playbooks are created during use.
