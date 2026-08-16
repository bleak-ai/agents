# Body: shipnotes-launch

## Hook (System 1)

Half my commits say "fix stuff" because it was 11pm and the test finally passed. My changelog used to inherit that. Now it does not, because the changelog never sees the commits.

## Proof (System 2)

shipnotes reads the merged diff and writes the entry from what actually changed: new flags, changed defaults, removed endpoints. Commit-message generators summarize what you said you did; shipnotes summarizes what the code did. First release out today, works on any GitHub repo.

## Close

Try it on your own repo's last release: `uvx shipnotes`.

Click-path checklist:

- **Action**: run the command once.
- **Target**: `uvx shipnotes` (install command from Post defaults in info.md).
- **Assumptions**: a terminal, uv installed, a repo with merged PRs. Acceptable for this segment.
- **Landing match**: the repo README opens with the same diff-not-commits claim. Verified.
