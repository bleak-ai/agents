# Exploration: export-contact-list

1. Open `https://app.acme-crm.test/contacts`. Already logged in (real Chrome profile). Page shows the contacts table.
2. Click the button with text "Export" (`button[data-testid="export-btn"]`). A format dialog appears.
3. Select "CSV" (`input[value="csv"]`), click "Download" (`button[type="submit"]`). Download starts.
4. Wait for the download to finish; file lands as `contacts.csv`.

Branching: on first visit a "What's new" modal appears; close it via `button[aria-label="Close"]` before step 2.

Site notes created at `sites/app.acme-crm.test/index.md` (Access: profile login persists; Navigation: contacts at /contacts; Selectors: export-btn testid; Gotchas: what's-new modal on first visit).
