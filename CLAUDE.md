# The Chief Prompt repo

This repo uses its own prompt. The chief-of-staff rules are in `.claude/rules/chief-of-staff.md`. Claude Code loads that file in every session. This file is for the rules of this repo only.

## Language

Talk to me in simple English (A2). Keep commands, error text, and technical terms exact.

## Rules for this repo only

- The product is the three lines to paste in `README.md` (install, install for a project that already has files, and update), the steps in `template/SETUP.md`, and the seven files in `template/` that the agent copies. "The prompt" means the lines and the steps together. A change to `template/` changes the rules of every project that uses the prompt, so treat it as code.
- The proof for every task is `python scripts/check.py`. It must pass before you call a task done.
- `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md`, `.claude/skills/chief-autopilot/SKILL.md`, `.claude/settings.json`, `.claude/agents/reviewer.md` and `.gitignore` in the repo root are exact copies of the files in `template/`. Change the file in `template/` first, then copy it. The check script fails if they differ.
- Keep the steps short. The check script fails when `template/SETUP.md` is over 400 words.
- When you change a rule, update `docs/limits.md` in the same change, and "Five limits to know" in `README.md` if one of the five changes.
- Keep `README.md` short. The check script fails over 140 lines. Long text goes into `docs/`.
- When you change `template/` or the prompt, add a line to `CHANGELOG.md` and set the "Last updated" line at the top of `README.md` to today's date and your model.
- `kb/` in this repo is public on GitHub. Write nothing private in it.
- When the first line of `README.md` changes, check the "About" text of the GitHub repo (`gh repo view --json description`) and propose the same words. The text is public, so ask before you change it.
- At each "Learn" review, also run the `sources-review` skill. It compares the pages in `kb/sources.md` with `template/` and `README.md`.
- If a rule in the template fails or confuses you, add a dated line to `kb/chief-prompt-lessons.md`: the rule, what happened, and why. Never prune this file.

@kb/status.md
@kb/todo.md
