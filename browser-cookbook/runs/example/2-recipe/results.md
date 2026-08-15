# Recipe proposal: export-contact-list

- **Recipe name**: export-contact-list
- **Script verdict**: script: yes. Fixed navigation, stable data-testid selectors, verifiable outcome (the CSV file). No content-dependent branching.
- **Parameters**: `out` (str, path for the CSV, default `contacts.csv`).
- **Read-only or mutating**: read-only.
- **Test plan**: run with defaults; expect the CSV to exist with a header row.

Script:

```python
import argparse
import pathlib

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("out", nargs="?", default="contacts.csv", help="Path for the CSV")
    args = parser.parse_args()

    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[0]
        page.goto("https://app.acme-crm.test/contacts")

        modal_close = page.locator('button[aria-label="Close"]')
        if modal_close.is_visible():
            modal_close.click()

        page.click('button[data-testid="export-btn"]')
        page.check('input[value="csv"]')
        with page.expect_download() as download_info:
            page.click('button[type="submit"]')
        download_info.value.save_as(args.out)

    out = pathlib.Path(args.out)
    assert out.exists(), f"{out} was not created"
    first_line = out.read_text().splitlines()[0]
    assert "name" in first_line.lower(), f"no header row: {first_line}"
    print(f"OK: {out} with header: {first_line}")


if __name__ == "__main__":
    main()
```
