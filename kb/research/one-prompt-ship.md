Status: research, not approved

# One prompt for the ship step

Draft from 2026-11-14. Nothing in `template/` is changed yet.

## The problem

The owner works in bypass mode and still gets many "allow" questions from Claude Code.

The cause is the ask rules in `.claude/settings.json`. The "Permission modes" page of the Claude Code docs says that a tool call matched by an explicit ask rule is not approved by itself in any mode, also not in `bypassPermissions`.

The session logs of this repo show which rules are hit. In 7 sessions with 1,384 tool calls, 88 Bash calls matched an ask rule:

| Ask rule | Calls |
| :- | :- |
| `Bash(git push *)` | 53 |
| `Bash(gh pr merge *)` | 29 |
| `Bash(rm *)` | 6 |
| `Bash(git merge *)` | 2 |
| The PowerShell rules, `Edit(/kb/approved/plan.md)` | 0 |

The logs hold the commands, not the questions. So this is the number of commands that match a rule, and not a count of the questions that were shown.

Almost all of it is the ship step. The rules say "ask me once for the whole step", and the owner says yes once in the chat. Then the agent runs the push and the merge as separate commands, and Claude Code asks again for each one. A failed try adds one more question. The 6 `rm` calls are all the cleanup of the clone in the update skill.

## The idea

The Permissions page says ask rules apply when any part of a compound command matches. Its example is that an ask rule for `git clean` "still prompts you" for `cd /tmp && git clean -f`. The page does not say how many questions a command with several matching parts gives. One question for the whole command is inferred. If that is right, one command with all parts joined by `&&` should give one question in place of two to four. Claude Code still asks, so nothing becomes less safe.

Not tested: nobody has counted the questions for one joined command yet.

## Test, 2026-11-14

PR 19 of this repo (this draft) was shipped with one joined command: push, create the PR, `gh pr checks --watch`, squash merge with branch delete, and the sync of local main. All parts worked at the first try. The owner got one question from Claude Code, in bypass mode. The checks took about 20 seconds, so long checks are still not tested.

## Possible wording

In `template/.claude/rules/chief-of-staff.md`, part "Approval", one new line after the line "When a branch is ready ...":

> After my yes, run the whole step as one shell command, joined with `&&`, so Claude Code asks me once. With GitHub: push, create the PR, wait for its checks, merge, delete the branch. Local only: switch to main, merge, delete the branch.

An example for GitHub, as the agent would write it:

```bash
git push -u origin my-branch && gh pr create --fill && gh pr checks --watch && gh pr merge --squash --delete-branch
```

An example for local only:

```bash
git checkout main && git merge my-branch && git branch -d my-branch
```

## What can go wrong

- **`gh pr checks --watch` in a repo with no checks.** It then ends with an error ("no checks reported"), and the `&&` stops the chain before the merge. The agent must leave this part out when the repo has no checks. The rule would have to say so, or the agent finds out at the first try and asks again.
- **Checks that start late.** Right after `gh pr create`, GitHub may not list the checks yet. In PR 18 of this repo the watch worked right after the create. One case is not proof.
- **Long checks.** A shell command of the agent stops after some minutes. With slow checks the chain ends before the merge, and the agent needs a second command, so a second question.
- **A failure in the middle.** With `&&`, the parts after the failure do not run. This fits the rule "stop only if something fails". The agent must then say which parts are done.
- **The question is longer.** The owner sees one long command in the question, not three short ones. It is harder to read.
- **Push only.** A push to a branch with no merge (for example for a parallel writer) still gets its own question. That is wanted.

## Cost

- One line in `template/.claude/rules/chief-of-staff.md` (64 lines now, the limit is 100), and its copy in the repo root.
- One sentence in `docs/limits.md`: the line "Claude Code can still show its own prompt for each of these commands" becomes "Claude Code still asks once for the joined command".
- A line in `CHANGELOG.md` and the "Last updated" line in `README.md`.
- It is a change in `template/`, so the reviewer reads it.
- It should be tried once in a real ship step before it goes into the template: count the questions.

## Other ways, not chosen

- **Remove the push and merge ask rules.** Then no question at all. But these rules are the only part of the prompt that Claude Code enforces, and the README promises them.
- **Keep it as it is.** Two to four questions for each PR.
- **Narrow the delete rule.** The logs show it is not the cause: 6 of 88.
