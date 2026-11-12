Status: research, not approved

# Autopilot mode (draft)

Date: 2026-11-13. Nothing here is in `template/` yet.

## What it is

A mode the user turns on. It is never the default. The agent works through `kb/todo.md` alone, inside the repo only, while the user is away. When the user is back, the agent shows what it did and asks the questions it saved.

## Decided (see `kb/approved/decisions.md`)

- The user turns it on. Without that, the normal rules apply.
- Local only. All work goes to one `autopilot` branch. No push.
- At an open question, the agent takes its own pick and continues on that line. It writes the question to a file. It builds the other options only when they are small (one task each), each on its own branch, for example `autopilot/q3-option-b`. Never options on top of options.
- When the user is back: one card per question. The card shows the agent's pick and the other branches. The user says which branches to delete.
- No task limit. It runs until `kb/todo.md` is empty.

## How it could work

1. The user types `/chief-autopilot`. This would be a new skill in `template/`, the seventh file. Only the user can start it.
2. The agent checks that the work tree is clean, then creates the `autopilot` branch from the current branch.
3. For each open task in `kb/todo.md`, in order: do the task, run the proof, commit on `autopilot`, tick the task, update `kb/status.md`.
4. At an open question: add it to `kb/research/autopilot-questions.md` with the options, the pick, the reason, and the names of the option branches. Then continue.
5. When `kb/todo.md` has no open task that the agent can do, it writes a short report at the top of `kb/research/autopilot-questions.md` and stops.
6. The user comes back and says "hello". The agent reads the questions file and asks the cards. After that the normal rules apply again, and the `autopilot` branch goes through the normal ship step: proof, reviewer, one approval.

## What stays forbidden in autopilot

- Everything the normal rules ask approval for outside the repo: sending email, messages, files or data, publishing, deploying, paying.
- `git push`, `gh repo create`, and any merge into `main`.
- Any edit of `kb/approved/plan.md`.
- A task that needs one of these is not done. The agent writes it to the questions file and goes to the next task.

## Problems found while writing this draft

- **The settings stop the session.** `.claude/settings.json` asks before `git merge` and before `rm` or `Remove-Item`. In autopilot nobody answers, so the session waits for ever. So the draft uses one branch with direct commits and no merge. The agent deletes no files; it lists them in the questions file. Option branches stay apart until the user decides.
- **Other permission questions.** Claude Code can also ask before a shell command that is not in the user's allow list. One such question stops the whole run. The user must start autopilot in a permission mode that does not ask. Which mode is safe here is not checked yet; read the permissions docs before this goes into the template.
- **"A week" is not one session.** A session ends when the work is done, when the usage limit is reached, or when the computer sleeps. A run over many days needs something that starts new sessions (a scheduled task). That is new machinery and is not in this draft.
- **It is advice.** Like most of the prompt, the agent can drift from these rules, and nobody sees it until the user is back. Only the deny and ask rules in the settings are enforced, and they still apply in autopilot.
- **The reviewer.** The normal rules say: reviewer before any code merge. Autopilot never merges, so the review happens once, when the user ships the `autopilot` branch. A long run gives one very big diff.

## Open points for the owner

1. **A failed check.** There is no task limit, so what happens when the proof fails? Proposal: the agent tries to fix it twice. If it still fails, it reverts that task's commits with `git revert`, marks the task as blocked in the questions file, and goes to the next task. Work that fails the proof never stays on `autopilot`.
2. **One branch, no merge, no delete.** As described above. Yes or no?
3. **Tasks that depend on a blocked task.** Proposal: skip them too, and say so in the questions file.
4. **Big diff at the end.** Proposal: one commit per task, so the user and the reviewer can read task by task.
5. **Many days.** Leave it out of the first version (proposal), or plan a scheduled task now?
6. **Where the mode lives.** A skill, `/chief-autopilot` (proposal), or a part of the rules file?

## If approved, what changes

- New file `template/.claude/skills/chief-autopilot/SKILL.md`, and a copy in the repo root.
- `README.md`: the first line (the promise), "How to use it", and "What it does, and what it does not".
- The prompt and the update skill must name the new file.
- `scripts/check.py`: checks for the new skill, like the ones for `chief-update`.
- `CHANGELOG.md` and the "Last updated" line.
