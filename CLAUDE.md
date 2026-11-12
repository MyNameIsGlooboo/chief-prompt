# The Chief Prompt repo

This repo uses its own prompt. The chief-of-staff rules are in `.claude/rules/chief-of-staff.md`. Claude Code loads that file in every session. This file is for the rules of this repo only.

## Language

Talk to me in simple English (A2). Keep commands, error text, and technical terms exact.

## Rules for this repo only

- The product is the prompt in `README.md` and the six files in `template/`. A change to `template/` changes the rules of every project that uses the prompt, so treat it as code.
- The proof for every task is `python scripts/check.py`. It must pass before you call a task done.
- `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md`, `.claude/settings.json`, `.claude/agents/reviewer.md` and `.gitignore` in the repo root are exact copies of the files in `template/`. Change the file in `template/` first, then copy it. The check script fails if they differ.
- Keep the prompt short. The check script fails over 400 words.
- When you change a rule, update the "What it does, and what it does not" part of `README.md` in the same change.
- `kb/` in this repo is public on GitHub. Write nothing private in it.
- At each "Learn" review, also run the `sources-review` skill. It compares the pages in `kb/sources.md` with `template/` and `README.md`.
- If a rule in the template fails or confuses you, add a dated line to `kb/chief-prompt-lessons.md`: the rule, what happened, and why. Never prune this file.

@kb/status.md
@kb/todo.md
