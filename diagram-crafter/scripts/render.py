"""Best-effort SVG screenshot via a locally installed headless Chrome.

Usage:
  render.py --check                 report whether a browser is available
  render.py <svg-path> <png-path>   screenshot the SVG to a PNG

Prints NO_BROWSER and exits 0 when no browser is found. Never exits
non-zero: rendering is an aid, not a requirement.
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


def find_browser():
    for candidate in CANDIDATES:
        if "/" in candidate:
            if Path(candidate).is_file():
                return candidate
        else:
            found = shutil.which(candidate)
            if found:
                return found
    return None


def viewbox_size(svg_text):
    match = re.search(r'viewBox="[\d.\s-]*?([\d.]+)\s+([\d.]+)"', svg_text)
    if match:
        return int(float(match.group(1))), int(float(match.group(2)))
    return 1520, 880


def main():
    args = [a for a in sys.argv[1:] if a]
    browser = find_browser()

    if args == ["--check"]:
        print(f"BROWSER: {browser}" if browser else "NO_BROWSER")
        return

    if len(args) != 2:
        print("USAGE: render.py --check | render.py <svg-path> <png-path>")
        return

    if browser is None:
        print("NO_BROWSER")
        return

    svg_path = Path(args[0]).resolve()
    png_path = Path(args[1]).resolve()
    if not svg_path.is_file():
        print(f"NO_FILE: {svg_path}")
        return
    png_path.parent.mkdir(parents=True, exist_ok=True)

    width, height = viewbox_size(svg_path.read_text(encoding="utf-8"))
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={png_path}",
        f"--window-size={width},{height}",
        svg_path.as_uri(),
    ]
    try:
        subprocess.run(cmd, capture_output=True, timeout=30, check=True)
    except (subprocess.SubprocessError, OSError) as exc:
        print(f"RENDER_FAILED: {exc}")
        return

    print(f"OK: {png_path}" if png_path.is_file() else "RENDER_FAILED: no output")


if __name__ == "__main__":
    main()
