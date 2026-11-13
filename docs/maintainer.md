# For the maintainer only

This part is for the owner of this repo. If you only use the prompt, skip it.

**Check.** `python scripts/check.py` checks the template files and the prompt: valid JSON, every deny and ask rule present for Bash and PowerShell, the reviewer's tools line, the rules file under 100 lines and with no import, the update skill and the autopilot skill (the name, that only the user can start it, the files the update replaces, and the actions autopilot must never do), `CLAUDE.md` with the Language line and both imports, the setup steps in `template/SETUP.md` under 400 words, the install line in `README.md` that points to them, the update line in `README.md` that points to the update skill, the root copies equal to the template, and the "Last updated" line at the top of `README.md` with the same date as the newest entry in `CHANGELOG.md`. It uses no model and costs nothing. GitHub Actions runs it on every push and pull request.

**This repo uses its own prompt.** The root `CLAUDE.md` holds only the rules for this repo. The root `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md`, `.claude/skills/chief-autopilot/SKILL.md`, `.claude/settings.json`, `.claude/agents/reviewer.md` and `.gitignore` are exact copies of the template files, and the check script fails if they differ. The `kb/` folder holds this repo's own status, tasks, and decisions.

**Feedback from my own projects.** This is only for me. It is not in the template, and other users do not need it. In my own projects I add this line to `CLAUDE.md`:

```markdown
- If a chief-of-staff rule fails or confuses you, add a dated line to kb/chief-prompt-lessons.md: the rule, what happened, and why. Never prune this file.
```

This file is separate from `kb/lessons.md`. `kb/lessons.md` is about the project, has a 20-line limit, and gets pruned. `kb/chief-prompt-lessons.md` is about this prompt and keeps every line.

Before I update this repo, I collect `kb/chief-prompt-lessons.md` from my projects. The lines show which rules fail in real use.

**Keeping it up to date.** [`kb/sources.md`](../kb/sources.md) lists the trusted pages. At each review (when Last review is over seven days old), the agent runs the [`sources-review`](../.claude/skills/sources-review/SKILL.md) skill: it reads the pages, compares them with `template/`, `README.md` and `docs/`, and writes what it finds to `kb/research/`. It proposes three changes at most, and I approve each one. I can also start it myself with `/sources-review`. This is advice, not enforced: it runs only when I open a session in this repo. The skill is for this repo only and is not in the template.
