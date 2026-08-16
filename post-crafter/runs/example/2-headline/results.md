# Headline workshop: shipnotes-launch

Formulas filtered for the problem-aware stage. Skipped: social-proof and number-anchor (no real numbers in info.md yet), scarcity (nothing scarce).

## Candidates

Scores: specificity / front-load / provable / angle fit / voice fit (max 25).

| # | Headline | Formula | S | F | P | A | V | Total |
|---|----------|---------|---|---|---|---|---|-------|
| 1 | Your commit messages do not matter for your changelog | counterintuitive | 4 | 5 | 5 | 5 | 4 | 23 |
| 2 | Stop writing changelogs from commits that say "fix stuff" | contrast-alternative | 5 | 4 | 5 | 5 | 4 | 23 |
| 3 | The changelog tool that never reads your commit messages | counterintuitive | 4 | 4 | 5 | 5 | 4 | 22 |
| 4 | shipnotes reads the diff, so your changelog stops lying | transformation | 4 | 4 | 4 | 5 | 4 | 21 |
| 5 | Write "fix stuff" commits. Ship a real changelog anyway | counterintuitive | 5 | 4 | 4 | 4 | 4 | 21 |
| 6 | How to ship a changelog without writing one | how-to | 3 | 5 | 4 | 4 | 4 | 20 |
| 7 | What does your changelog say when your commits say nothing | question | 4 | 3 | 4 | 5 | 4 | 20 |
| 8 | From empty CHANGELOG.md to release notes in one command | transformation | 4 | 4 | 4 | 4 | 3 | 19 |
| 9 | Changelog generators trust your commits. That is the bug | contrast-alternative | 4 | 3 | 4 | 4 | 4 | 19 |
| 10 | I shipped a release with an empty changelog. Never again | story | 3 | 4 | 4 | 4 | 4 | 19 |
| 11 | Your diff already wrote your changelog | curiosity-gap | 4 | 4 | 3 | 4 | 3 | 18 |
| 12 | The maintainer's way out of changelog debt | unity-identity | 3 | 3 | 4 | 4 | 3 | 17 |
| 13 | Why "fix stuff" commits break every changelog generator | question | 4 | 3 | 3 | 4 | 3 | 17 |
| 14 | A changelog your users can actually read | curiosity-gap | 2 | 4 | 3 | 3 | 4 | 16 |
| 15 | Release notes without the Friday-evening scramble | loss-aversion | 3 | 3 | 3 | 3 | 3 | 15 |

## Red team

- #1 "Your commit messages do not matter for your changelog": "Sure they do, mine are fine. This is a tool for sloppy people." Survives: the follow-up hook names the real case (squash merges, "fix stuff" under deadline), which every maintainer has.
- #2 "Stop writing changelogs from commits that say fix stuff": "So fix your commit discipline instead of installing a tool." Survives: discipline does not fix past history; the diff is already there.
- #3 "The changelog tool that never reads your commit messages": "Then what does it read, marketing air?" Survives: the answer (the diff) is one word away, and the curiosity is the point.
- #4 "shipnotes reads the diff, so your changelog stops lying": "My changelog does not lie, it is just empty." Revised once to "so your changelog stops being empty"; still weaker than #1. Dropped, #6 promoted.
- #5 "Write fix stuff commits. Ship a real changelog anyway": "This glorifies bad habits." Survives: it is a joke the segment makes about itself.

## Selected headline

The user picked #1.

## Variations

1. Shorter: "Commit messages do not matter for changelogs."
2. Frame shift ("you" to "I"): "I stopped letting commit messages write my changelog."
3. With a detail: "Your commit messages do not matter: shipnotes reads the diff."

## Final headline

Your commit messages do not matter for your changelog.
