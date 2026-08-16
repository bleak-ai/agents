# Sites

Per-site knowledge, shared by every recipe and run on that domain. One folder per domain (e.g. `app.example.com/`). Created on first contact, updated on every contact, including failed runs.

Each site folder contains:

- `index.md`: the map, with exactly these sections: **Access** (login flow, session quirks), **Navigation** (how to reach the areas that matter), **Selectors** (stable anchors that survive redesigns, each with its anchor strategy: `text-label`, `aria-role`, `stable-id`, or `css-class`, and an overall durability rating), **Gotchas** (modals, lazy loading, anti-bot behavior).
- `blocks/*.md`: reusable procedure fragments the AI reads (e.g. `login.md`, `search.md`). Created when a second recipe needs the fragment.
- `lib.py`: Python helpers scripts import (e.g. `login(page)`). One fix here heals every script on the site.
- `selftest.py`: attaches over CDP, loads each page the site's scripts depend on, asserts every recorded anchor still resolves. Read-only, no mutations. Exit 0 when all pass, exit 1 and prints dead anchors.

## Contents

_(no sites yet; folders appear on first contact)_
