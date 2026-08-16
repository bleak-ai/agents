# Assembled post: shipnotes-launch

Format: text only.

---

Your commit messages do not matter for your changelog.

Half my commits say "fix stuff" because it was 11pm and the test finally passed. My changelog used to inherit that. Now it does not, because the changelog never sees the commits.

shipnotes reads the merged diff and writes the entry from what actually changed: new flags, changed defaults, removed endpoints. Commit-message generators summarize what you said you did; shipnotes summarizes what the code did. First release out today, works on any GitHub repo.

Try it on your own repo's last release: `uvx shipnotes`.

---

Saved to `posts/2001-01-01-shipnotes-launch.md` with frontmatter: product shipnotes, goal launch, angle "commit messages do not matter, shipnotes reads the diff", headline_formula counterintuitive, persuasion_levers [pattern-interrupt, identity], format text.
