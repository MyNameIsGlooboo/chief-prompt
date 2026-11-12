# Chief prompt lessons

One dated line per rule that failed or confused the agent: the rule, what happened, and why. Never prune this file.

- 2026-11-13: Rule "Copy them exactly" (prompt step 1). In this repo `CLAUDE.md` could not be an exact copy, because the repo needs its own rules too. It imports `template/CLAUDE.md` and adds a short part. Why: the prompt has no word on a project that needs extra rules in `CLAUDE.md`.
- 2026-11-13: Rule "Create kb/ as CLAUDE.md describes" (prompt step 3). `kb/research/` is empty at the start, and git does not keep an empty folder. Why: the rule does not say what to do with an empty folder.
