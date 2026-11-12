# Chief prompt lessons

One dated line per rule that failed or confused the agent: the rule, what happened, and why. Never prune this file.

- 2026-11-13: Rule "Copy them exactly" (prompt step 1). In this repo `CLAUDE.md` could not be an exact copy, because the repo needs its own rules too. It imports `template/CLAUDE.md` and adds a short part. Why: the prompt has no word on a project that needs extra rules in `CLAUDE.md`.
- 2026-11-13: Rule "It asks me before `git push`, `git merge`, `gh pr merge` ... deleting files" (Approval). For each of three small changes the agent asked three times: open the PR, merge, delete the branch. The owner said it should be one step with one approval. Why: the rule lists the actions one by one and has no word on asking for them together.
- 2026-11-13: Rule "Create kb/ as CLAUDE.md describes" (prompt step 3). `kb/research/` is empty at the start, and git does not keep an empty folder. Why: the rule does not say what to do with an empty folder.
- 2026-11-13: Rule "Copy them exactly and do not rewrite them. If one of these files already exists here ... stop and ask me" (prompt step 1). In a project with files, the agent stops at once (almost every project has a `.gitignore`), and the rule gives no way on but overwrite or skip. The agent also told the owner twice to update a project by copying the new `CLAUDE.md` over the old one, which would delete the Language line and the project's own rules. Why: the template mixed rules the prompt owns with lines the project edits, in one file.
