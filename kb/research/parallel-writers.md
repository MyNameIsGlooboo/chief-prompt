Status: research, not approved

# Draft: the chief gives tasks to parallel writers

Date: 2026-11-14.

## The problem

The owner uses the prompt in a real project. Two things went wrong there:

- The chief session was almost always busy, so the owner could not talk to it.
- The work was slow. The owner's limit is time, not usage.

The rules allow parallel writers today, but the chief does not start them by itself ("Use them only for long, parallel, or clean-context work"). And the owner must read and merge each writer branch ("I read and merge those myself").

## What the owner decided

These are in `kb/approved/decisions.md` (2026-11-14):

1. The chief may give tasks to parallel background writers and stays free to talk.
2. The chief brings the work of its own writers together itself, with no question, on a work branch. One yes for the ship step to main.
3. It uses `git cherry-pick`, not `git merge`. The ask rule for `git merge` stays in the settings.
4. Autopilot works the same way.

## The design

The chief is the manager:

- It talks to the owner, cuts work into tasks, writes the briefs, and checks each result.
- Only the chief writes `kb/`.
- It writes code itself only when the task is small (a few minutes), when the task needs the owner's answers on the way, or when the task builds on work that is not on main yet.

A writer is a background agent:

- One task, one writer, one worktree, one branch, one commit.
- Three writers at most at one time.
- It runs the proof before it commits, and reports in a few lines.
- It does not touch `kb/`, and it does not push.

Against conflicts:

- Two tasks that share files never run at the same time. The second waits.
- A writer's worktree starts from the default branch (Claude Code docs, "isolation: worktree"), not from the work branch. So a task that builds on work that is not on main waits, or the chief does it.
- The chief picks one commit at a time onto the work branch, and runs the proof after each pick.

The ship step does not change: when the work branch is ready (proof passed, reviewer found no blocking problem), the chief asks once for push, PR, merge and branch delete.

## Draft of the rule text

In "Approval", the line about parallel writers becomes:

```text
- You bring the work of your own background writers together yourself, with no question: pick each writer's commit onto your work branch with `git cherry-pick`, one at a time, and run the proof after each pick. The work branch then follows the rule for a ready branch.
```

"Background agents" becomes:

```text
- Keep the chat free for me. Give an open task to a background writer when its "done when" is clear and it shares no files with a task that is running. Do a task yourself when it takes only a few minutes, when it needs my answers on the way, or when it builds on work that is not on main yet.
- Before you start writers, tell me in one line which tasks run now and which wait.
- Each writer gets its own worktree and branch, and makes one commit for its task. Three writers at most at one time. A writer does not push, and does not touch `kb/`: you update it.
- Two agents never write the same files.
- Each agent gets a full brief (goal, files, done when, and for a writer the proof to run), because it cannot see the chat.
- Say in one line what each is doing. When it finishes, check its result yourself, then tell me in a few lines: what it found or changed, and what it could not check.
- If a pick has a conflict, run `git cherry-pick --abort` and give the task back to its writer with the new state. If the proof fails after a pick, take the commit back with `git revert` and do the same.
- Use other background agents only for long, parallel, or clean-context work, because each costs my usage.
```

## Draft of the autopilot changes

- "For each open task in kb/todo.md, in order" becomes: take the next open tasks that share no files and do not build on each other, three at most, and give each to a writer. Tasks that cannot run in parallel run one after the other, as today.
- Each writer's commit is picked onto `autopilot`. The rule "one commit per task" stays true.
- "Never in autopilot" stays: no push, no `git merge`, no delete. So the worktrees and the branches of the writers stay until the owner is back, and the report lists them.
- A writer whose proof fails twice: its branch stays, the task is written to the questions file as blocked. No stash is needed, because the work is on its own branch.

## Open points for the owner

1. A `writer` agent file in the template (`.claude/agents/writer.md`), as the eighth file. It holds the fixed rules of a writer, so each brief is shorter. My pick: yes. It changes `template/SETUP.md`, the update skill, the check script and the docs.
2. The model of the writer. Options: `sonnet` (cheaper), or the same model as the chief. My pick: `sonnet`.
3. `memory: project` for the writer, so it keeps notes about the project. My pick: no at first, because it adds a folder that the prompt must explain.
4. Who removes the worktrees and the branches of the writers after the ship step. My pick: the chief, in the same joined ship command, because they are its own.

## Test

Not done yet.

## Limits to write into docs/limits.md

- Cognition found that parallel writers do not work well (see `docs/why-one-agent.md`). This rule makes them the normal case, with the limits "no shared files" and "three at most".
- A writer does not see the chat. A task with a weak "done when" gives weak work.
- Each writer starts with an empty memory and reads the files again, so usage goes up.
- The permission questions of each writer appear in the main chat. In autopilot one question stops the run.
- `git cherry-pick` goes around the ask rule for `git merge`. This is the owner's choice. Main is still behind the ask rules for push and merge.
- The chief is not free while it checks a result or runs the ship step.
