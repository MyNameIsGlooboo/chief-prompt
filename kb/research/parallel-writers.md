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
5. The line `.claude/worktrees/` in the template `.gitignore` (found in the test). My pick: yes. Without it, the autopilot skill and the update skill stop while a worktree exists.

## Feedback from the chief of a real project

The owner showed the five open points to the chief session of a real project (2026-11-14). It agreed with all five picks. These points from it go into the build:

- The `writer` agent has no `Agent` tool, so it cannot start agents itself.
- The brief still gives goal, files and done when. Only the fixed rules move into the agent file.
- Model: `sonnet` is the default in the agent file. For a task that needs judgement, the chief names a stronger model in the call. The model in the call comes before the model in the agent file (Agent tool of Claude Code: "Takes precedence over the agent definition's model frontmatter"). Its example: a wrong date in 33 records that only the reviewer found.
- The reviewer is not weaker than the writer.
- "No shared files" is the chief's job before it starts writers. It also counts files that every task changes on the side, such as an index file. Its example: each task wrote the same `index.json`, so three tasks needed one writer, not three.
- A fixed report from the writer: what changed, the output of the proof, what it could not check. The chief runs the reviewer, not the writer.
- Clean-up: `git worktree remove` comes before the delete of the branch, because git refuses to delete a branch that a worktree still uses. Never `--force`: a worktree with work that is not committed must stop the command. The ship question names these deletes too.
- `git add -A` would add the worktree folders to a commit. One more reason for the `.gitignore` line.
- The first line of the rules file says "one main agent, no team". With writers as the normal case, the line needs new words.

Two points where the draft does not follow it:

- "Never `-D`". With `git cherry-pick` the writer's branch is never merged, so `git branch -d` always refuses (seen in the test). The safe way: delete with `-D` only after a check that every commit of the writer is on the work branch. `git cherry <work branch> <writer branch>` prints a line that starts with `+` for each commit that is not there. No such line, then `-D`.
- "A background writer cannot answer a permission question, so the question stops it." The Claude Code docs say the question comes up in the main session and names the writer (sub-agents page, checked 14 Nov 2026). So the owner can answer it there. In autopilot nobody answers, and there it does stop the run. Its conclusion still holds: a writer never pushes, merges or deletes, so it does not reach such a question.

One point it could not check: the agent file can force the worktree. The docs have the frontmatter field `isolation: worktree` (same page).

## Test

Done on 2026-11-14 in this repo, in the Claude desktop app, with two writers at the same time (`general-purpose` agents, model `sonnet`, `isolation: worktree`). Each writer added one small file and made one commit.

What worked:

- Both writers ran in the background, and the chief could go on. They took 9 and 11 seconds.
- Each got its own worktree in `.claude/worktrees/agent-<id>` and its own branch `worktree-agent-<id>`.
- Both worktrees started from main (`246941a`), not from the chief's branch (`parallel-writers-draft`). So a writer does not see work that is not on main.
- `python scripts/check.py` passed in each worktree.
- The chief picked both commits onto a test branch with `git cherry-pick`, and the check passed after each pick.
- Claude Code asked no permission question: not for the writers' commands, not for `git cherry-pick`, not for `git worktree remove`, not for `git branch -D`.

What the test found:

1. **A writer is not cheap.** Each writer used about 82,000 tokens for a task of two lines and four tool calls. Most of it is the start of the agent, not the work. So "do a task yourself when it takes only a few minutes" matters for usage, and a small task must stay with the chief.
2. **`.claude/worktrees/` shows up in `git status`.** While a writer's worktree exists, `git status --short` prints `?? .claude/worktrees/`. The autopilot skill and the update skill stop when `git status --short` shows anything. So the template `.gitignore` needs the line `.claude/worktrees/`.
3. **A writer adds the Co-Authored-By line to its commit by itself.** One of the two reported it. This is fine, but the picked commit keeps it.
4. **Clean-up is three commands for each writer**: `git worktree remove`, `git branch -D` for its branch (`-d` refuses, because the branch is not merged, only picked). The empty folder `.claude/worktrees/` stays.

What the test did not cover:

- A pick with a conflict, and a proof that fails after a pick.
- A real task with real code, and the quality of a writer's work on the cheaper model.
- Three writers, and writers that run for many minutes.
- Autopilot with writers.
- A session in a terminal, and a permission mode other than the one of this session.

## Limits to write into docs/limits.md

- Cognition found that parallel writers do not work well (see `docs/why-one-agent.md`). This rule makes them the normal case, with the limits "no shared files" and "three at most".
- A writer does not see the chat. A task with a weak "done when" gives weak work.
- Each writer starts with an empty memory and reads the files again, so usage goes up.
- The permission questions of each writer appear in the main chat. In autopilot one question stops the run.
- `git cherry-pick` goes around the ask rule for `git merge`. This is the owner's choice. Main is still behind the ask rules for push and merge.
- The chief is not free while it checks a result or runs the ship step.
