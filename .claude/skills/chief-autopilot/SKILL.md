---
name: chief-autopilot
description: Work through kb/todo.md alone while the user is away. Local only, on one autopilot branch, with no push, no merge and no delete. Open questions are saved for the user.
disable-model-invocation: true
---

Autopilot: work through `kb/todo.md` alone while I am away. The mode is on for this run only. It ends when you stop, or when I write to you again.

While it is on, do not ask me anything and do not wait for me. This comes before the "ask me" rules in `.claude/rules/chief-of-staff.md`. An action that needs my approval is not done: write it to the questions file and go on.

## Before you start

I am still here for these steps, so you may ask.

1. If this folder is not a git repo, stop and tell me. Run `git status --short`. If it shows anything, stop and ask me.
2. If a branch named `autopilot` exists, stop and ask me. If not, create it from the current branch and switch to it.
3. Create `kb/research/autopilot-questions.md`. Its first line is "Status: research, not approved".
4. Tell me in one message: the open tasks you will try, the tasks you cannot do alone and why, and this warning: "A permission question from Claude Code stops the run until you answer. Auto mode asks the fewest questions." Then start. Do not wait for an answer.

## For each open task in kb/todo.md, in order

1. Skip the task if it needs something from "Never in autopilot", or if it builds on a task that is blocked or skipped. Write the task and the reason to the questions file.
2. Do the task. Run the proof from the plan. If there is no proof, use the task's "done when" and say so in the questions file.
3. If the proof fails, fix it and run it again, two times at most. If it still fails, run `git stash push -u -m "autopilot: <task>"`, write the task, the error and the stash name to the questions file as blocked, and go to the next task. Work that fails the proof never gets a commit.
4. If the proof passes, tick `kb/todo.md`, update `kb/status.md`, and make one commit for this task.

## An open question

- Take your own pick and continue on `autopilot`. Write to the questions file: the question, the options, your pick, and the reason.
- Build another option only if it is small, one task at most. Give it its own branch, `autopilot/q<number>-<option>`, then switch back to `autopilot`. Never build options on top of an option branch.
- Your picks are not my decisions. Do not write them to `kb/approved/`.

## Never in autopilot

- `git push`, `git merge`, `gh pr merge`, `gh repo create`, deleting a file, and any edit of `kb/approved/plan.md`. Claude Code asks me before each of these, and nobody is there to answer. List a file that should be deleted in the questions file.
- Sending email, messages, files or data to other people or outside services, publishing, deploying, and paying.
- Any change outside this project folder.
- Changes to hooks, settings, permissions or agents.

## When no task is left that you can do

Write a short report at the top of the questions file: tasks done, tasks blocked, tasks skipped, stashes, option branches, and files to delete. Commit it and stop.

## When I am back

1. Read the questions file and show me the report.
2. Ask one card per question: your pick, the other options, and their branches. Log my answers in `kb/approved/decisions.md`.
3. Delete the option branches and drop the stashes that I name. Ask before any other delete.
4. The `autopilot` branch now follows the normal rule for a ready branch: proof, reviewer, one approval.

## Limits

- This skill is advice. Only the deny and ask rules in `.claude/settings.json` are enforced.
- One run is one session. It ends when the tasks are done, when the usage limit is reached, or when the computer sleeps.
