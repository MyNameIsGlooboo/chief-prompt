# The Chief Prompt repo

This repo uses its own prompt. The standing rules come from the template, so there is one source:

@template/CLAUDE.md

## Rules for this repo only

- The product is the prompt in `README.md` and the four files in `template/`. A change to `template/` changes the rules of every project that uses the prompt, so treat it as code.
- The proof for every task is `python scripts/check.py`. It must pass before you call a task done.
- `.claude/settings.json`, `.claude/agents/reviewer.md` and `.gitignore` in the repo root are exact copies of the files in `template/`. Change the file in `template/` first, then copy it. The check script fails if they differ.
- Keep the prompt short. The check script fails over 400 words.
- When you change a rule, update the "What it does, and what it does not" part of `README.md` in the same change.
- `kb/` in this repo is public on GitHub. Write nothing private in it.
- At each "Learn" review, also read the pages in `kb/sources.md` and follow the rules at the top of that file.
- If a rule in the template fails or confuses you, add a dated line to `kb/chief-prompt-lessons.md`: the rule, what happened, and why. Never prune this file.

@kb/status.md
@kb/todo.md
