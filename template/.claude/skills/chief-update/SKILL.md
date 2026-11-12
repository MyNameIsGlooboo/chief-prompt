---
name: chief-update
description: Update the chief-of-staff files of this project to the newest version from the chief-prompt repo. Replaces only the two files the prompt owns and adds missing lines to the others.
disable-model-invocation: true
---

Update this project to the newest version of the chief prompt. The source is the `template/` folder of https://github.com/MyNameIsGlooboo/chief-prompt.

Two files belong to the prompt, and you replace them. All other files belong to me: never replace or rewrite them, add only what is missing.

## Steps

1. If this folder is not a git repo, stop and tell me to run `git init` and commit my work first. Run `git status --short`. If it shows anything, stop and ask me. Note the name of the current branch, then create a new branch and switch to it.
2. Clone the repo to a temporary folder outside this project. If git is missing or the clone fails, stop and tell me. Check that the clone's `template/` folder has all six files: `CLAUDE.md`, `.gitignore`, `.claude/settings.json`, `.claude/agents/reviewer.md`, `.claude/rules/chief-of-staff.md` and `.claude/skills/chief-update/SKILL.md`. If one is missing, remove the clone, do step 12, and tell me. Change nothing in this project before this check has passed.
3. Replace these two files with the copies from `template/`, exactly:
   - `.claude/rules/chief-of-staff.md`
   - `.claude/skills/chief-update/SKILL.md` (this file). Finish this run with the steps you have already read.
4. `.claude/settings.json`: add each deny rule and ask rule that is in the template and not here. Keep every rule that is here, also one that is not in the template. If the file is missing, copy it.
5. `.gitignore`: add the lines that are in the template and not here. If the file is missing, copy it.
6. `.claude/agents/reviewer.md`: if it is missing, copy it. If it differs from the template, show me the difference and ask which one to keep. Do not merge the two yourself.
7. `CLAUDE.md`: check that it has the Language part and that it ends with the lines `@kb/status.md` and `@kb/todo.md`. Add what is missing and change nothing else. If it still holds chief-of-staff rules from the first version of the prompt (parts such as "Approval", "Save as you go" or "Learn"), show me those parts and ask before you remove them.
8. Remove the clone.
9. Run `git status --short`. If it shows nothing, do step 12, say "Already up to date", and end.
10. If it shows something, list each file and what you did to it. Show me `git diff` for the changed files. `git diff` does not show new files, so show each new file in full. If `.claude/settings.json` is new or changed, show me the whole file. Then ask me: commit, yes or no?
11. If I say yes, commit on the new branch. Tell me to open a new session, because Claude Code loads rules, settings and skills when a session starts. If the skill file itself changed in step 3, also tell me to type `/chief-update` once more in that new session, because the newer skill can have steps that this run did not do. The new branch then follows the normal rule for a ready branch.
12. Undo, for a no and for a stop: run `git restore .`, delete only the files that this run created, switch back to the branch from step 1, and delete the new branch. Then tell me that the project is as it was before.

## Limits

- Do not touch `kb/`, the plan, or any file not named above.
- Do not remove a rule or a line because the template no longer has it. Tell me about it and let me decide.
- If a step fails after step 2, stop and tell me what is done and what is not. Ask me: undo with step 12, or keep the changes so I can look. Do not leave the project half updated without saying so.
