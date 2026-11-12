---
name: chief-update
description: Update the chief-of-staff files of this project to the newest version from the chief-prompt repo. Replaces only the two files the prompt owns and adds missing lines to the others.
disable-model-invocation: true
---

Update this project to the newest version of the chief prompt. The source is the `template/` folder of https://github.com/MyNameIsGlooboo/chief-prompt.

Two files belong to the prompt, and you replace them. All other files belong to me: never replace or rewrite them, add only what is missing.

## Steps

1. Run `git status`. If there are changes that are not committed, stop and ask me. Work on a new branch.
2. Clone the repo to a temporary folder outside this project. If git is missing or the clone fails, stop and tell me. Use only its `template/` folder.
3. Replace these two files with the copies from `template/`, exactly:
   - `.claude/rules/chief-of-staff.md`
   - `.claude/skills/chief-update/SKILL.md` (this file). Finish this run with the steps you have already read.
4. `.claude/settings.json`: add each deny rule and ask rule that is in the template and not here. Keep every rule that is here, also one that is not in the template. If the file is missing, copy it.
5. `.gitignore`: add the lines that are in the template and not here. If the file is missing, copy it.
6. `.claude/agents/reviewer.md`: if it is missing, copy it. If it differs from the template, show me the difference and ask which one to keep. Do not merge the two yourself.
7. `CLAUDE.md`: check that it has the Language part and that it ends with the lines `@kb/status.md` and `@kb/todo.md`. Add what is missing and change nothing else. If it still holds chief-of-staff rules from the first version of the prompt (parts such as "Approval", "Save as you go" or "Learn"), show me those parts and ask before you remove them.
8. Remove the clone.
9. If nothing changed, say "Already up to date" and stop. Delete the empty branch.
10. If something changed, list each file and what you did to it, and show me `git diff`. If `.claude/settings.json` changed, show me the whole file. Wait for my yes before you commit.
11. After the commit, tell me to open a new session, because Claude Code loads rules, settings and skills when a session starts.

## Limits

- Do not touch `kb/`, the plan, or any file not named above.
- Do not remove a rule or a line because the template no longer has it. Tell me about it and let me decide.
- If a step fails, stop and tell me what is done and what is not. Do not leave the project half updated without saying so.
