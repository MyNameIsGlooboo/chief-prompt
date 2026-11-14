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
2. If `kb/research/autopilot-questions.md` exists, an earlier run is not closed: do the part "When I am back" and do not start a new run. If only a branch named `autopilot` exists, stop and tell me to merge or delete it first. If neither exists, create the branch `autopilot` from the current branch and switch to it.
3. Create `kb/research/autopilot-questions.md`. Its first line is "Status: research, not approved". In `kb/status.md`, set Next step to: "Autopilot ran. Read `kb/research/autopilot-questions.md` and do the part 'When I am back' in `.claude/skills/chief-autopilot/SKILL.md`." Keep that line until I am back, because a new session finds the run only through it. Commit both files.
4. Tell me in one message: the open tasks you will try, the tasks you cannot do alone and why, and this warning: "A permission question from Claude Code stops the run until you answer. Auto mode asks the fewest questions. With `"denyInsteadOfPrompting": true` under `permissions` in a file passed with `--settings`, Claude Code refuses such an action and the run goes on (v2.1.319 or later). While it is on, a push, a merge and a delete are refused also after your yes, so do 'When I am back' in a session without it." Only I set that setting, never you. Then start. Do not wait for an answer.

## The questions file

Each time you write to `kb/research/autopilot-questions.md`, commit that file alone at once: `git commit -m "autopilot: note" -- kb/research/autopilot-questions.md`. Then a stash can never take a note with it.

## For each open task in kb/todo.md, in order

1. Skip the task if it needs something from "Never in autopilot", or if it builds on a task that is blocked or skipped. Write the task and the reason to the questions file.
2. Do the task. Run the proof from the plan. If there is no proof, use the task's "done when" and say so in the questions file.
3. If the proof fails, fix it and run it again, two times at most. If it still fails, run `git stash push -u -m "autopilot: <task>"`, write the task, the error and the stash name to the questions file as blocked, and go to the next task. Work that fails the proof never gets a commit.
4. If the proof passes, tick `kb/todo.md`, add the task to Done in `kb/status.md`, and make one commit for this task.

## Tasks for writers

To be faster, give tasks to background writers as your rules say in "Background agents": three at most at one time, only tasks that share no files and do not build on each other. Do all other tasks yourself, with the steps above.

1. A writer starts from main, not from `autopilot`. So give it only a task that needs nothing from this run.
2. When a writer reports a commit, pick it onto `autopilot` as your rules say in "Approval": first commit your own task or finish it, so that `git status --short` shows nothing, then check the commit with `git show --stat`, then `git cherry-pick`, then the proof. A commit that touches `kb/`, `.claude/`, or a file outside its brief is not picked: write it to the questions file as blocked. If the proof passes, tick `kb/todo.md` and add the task to Done in `kb/status.md` in a second commit, `autopilot: tick <task>`.
3. If a writer reports no commit, or the pick has a conflict (`git cherry-pick --abort`), or the proof fails after the pick (`git revert`), write the task, the error and the writer's branch to the questions file as blocked. Its work stays on its branch.
4. A permission question from a writer stops the run too. So a writer gets no task that needs something from "Never in autopilot".

## An open question

- Take your own pick and continue on `autopilot`. Write to the questions file: the question, the options, your pick, and the reason.
- Build another option only if it is small, one task at most, and in this order:
  1. Finish the task with your pick and commit it on `autopilot`.
  2. Right after that commit, create the option branch from the commit before it: `git switch -c autopilot-q<number>-<option> HEAD~1`. Do not use a `/` in the name, because git refuses `autopilot/...` while the branch `autopilot` exists.
  3. Build the option, run the proof, and commit there. If the proof fails twice, stash the work as in the task steps.
  4. Run `git status --short`. Only when it shows nothing, run `git switch autopilot`.
- Never build options on top of an option branch.
- Your picks are not my decisions. Do not write them to `kb/approved/`.

## Never in autopilot

- `git push`, `git merge`, `gh pr merge`, `gh repo create`, deleting a file, and any edit of `kb/approved/plan.md`. Claude Code asks me before each of these, and nobody is there to answer. List a file that should be deleted in the questions file.
- Sending email, messages, files or data to other people or outside services, publishing, deploying, and paying. A search, and opening or reading a page, is not sending.
- Asking me to pass a CAPTCHA or a login on a page. If you cannot read a page without me, write its address and the reason to the questions file, and go on without the page.
- Removing a worktree or a branch of a writer. They stay until I am back.
- Any change outside this project folder.
- Changes to hooks, settings, permissions or agents.

## When no task is left that you can do

Write a short report at the top of the questions file: tasks done, tasks blocked, tasks skipped, stashes, option branches, the worktrees and branches of writers, and files to delete. Commit it and stop.

## When I am back

1. Read the questions file and show me the report.
2. Ask one card per question: your pick, the other options, and their branches. Log my answers in `kb/approved/decisions.md`.
3. Delete the option branches and drop the stashes that I name. Leave the worktrees and the branches of the writers for the ship step in step 5. For a blocked writer, ask me now: give the task back to it, or remove its worktree and branch. Its work is only on its branch. Ask before any other delete.
4. Move the questions file to `kb/research/autopilot-questions-YYYY-MM-DD.md` with `git mv`, set Next step in `kb/status.md` to the real next step, and commit. The run is now closed.
5. The `autopilot` branch now follows the normal rule for a ready branch: proof, reviewer, one approval. After the merge and the delete of the branch, a new run can start.

## Limits

- This skill is advice. Only the deny and ask rules in `.claude/settings.json` are enforced.
- One run is one session. It ends when the tasks are done, when the usage limit is reached, or when the computer sleeps.
