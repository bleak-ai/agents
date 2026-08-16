# Design system

The core asset of this module: every SVG draft applies these files without
asking, and style is never negotiated per run. Edits happen only when the
user corrects the same style decision twice; then propose the change
through the question tool and date it at the bottom of the edited file.

- `palette.md`: colors and their assignment rules.
- `typography.md`: family stack and the size scale.
- `layout.md`: canvas, spacing, cards, arrows, story strip.
- `icons.md`: inline Lucide defs to copy into the SVG defs.
