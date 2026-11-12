# Decisions

- 2026-11-13: Ship the rules as files in `template/`; the prompt copies them. Reason: the same rules in every project, and a script can check them.
- 2026-11-13: Check the files with a script and no model (`scripts/check.py`), run by GitHub Actions. Reason: testing must cost nothing.
- 2026-11-13: No paid test runs on fake projects, and no smoke run per model release. Reason: cost.
- 2026-11-13: No manual live-session check of the settings rules for now. Reason: owner's choice.
- 2026-11-13: Feedback on the prompt comes from the owner's own projects, in `kb/chief-prompt-lessons.md`. It is for the owner only and is not in the template. Reason: real use is better evidence than fake projects, and other users do not need it.
- 2026-11-13: `kb/chief-prompt-lessons.md` is a separate file from `kb/lessons.md`. Reason: `lessons.md` has a 20-line limit and gets pruned.
- 2026-11-13: This repo uses its own prompt. Reason: the owner's first real project for feedback.
