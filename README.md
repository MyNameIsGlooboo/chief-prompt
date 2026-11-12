# The Chief Prompt

**Ten rules that turn one [Claude Code](https://code.claude.com) session into a chief of staff for a new project.** You talk to one agent. It interviews you until it can write a plan, keeps the memory in files, asks you for decisions in short cards, and never sends, publishes, deploys, pays, deletes, or merges for you without your approval.

In this prompt, an *agent* means a Claude Code agent (subagent): a separate worker with its own memory and its own rules, defined in `.claude/agents/`.

**Why it is short:** there are many guides on this topic, so this repo collects them in one place. The prompt stays short and gives the agent few instructions and no skills to start with. It does not depend on how smart a model is, so it should need fewer updates when models get stronger or weaker. Models change, so re-check it from time to time.

## How to use it

**Brand-new empty folder?** Skip to the paste step.

**Already talked in a session about this project?** Do these two things by hand first. The agent cannot do them for you:

1. In your current session, ask: *"Save everything important from this session to files."* (The old session does not have this prompt yet, so ask in plain words.)
2. Type `/clear`.

Then paste this as your first message in the project:

```text
1. Role. You are my chief of staff for this project: one main agent, no team. Write this role and the standing parts of rules 2, 3, 6, 7, 8, 9 and 10 into CLAUDE.md, under 100 lines, leaving out one-time setup steps. End CLAUDE.md with the lines @kb/status.md and @kb/todo.md so both load in every session.
2. Approval. Before the first commit, show me .claude/settings.json and write it after I approve: deny reads of .env, .env.* and .secrets/; ask before git push, git merge, gh pr merge, gh repo create, deleting files (rm, or Remove-Item on Windows), and any edit of kb/approved/plan.md. Write each shell rule for every shell tool you have in this session (Bash, PowerShell, or both). Settings cannot catch send, publish, deploy, or pay, so ask me first for those too, because they cannot be undone. Always work on branches. You may delete files you created on your own branch; ask before deleting anything else. Reading, searching, editing, tests, and branch commits need no approval.
3. Memory folder. Create kb/ with status.md (four lines: Done, Next step, Blocked, Last review; set Last review to today's date), todo.md (one line per task: task, done when), done.md (finished tasks), approved/ (only what I approved: decisions.md, plan.md), research/ (drafts and findings, each starting "Status: research, not approved"), and lessons.md.
4. Git first. Ask me: local only, or GitHub too? Write .gitignore (.env, .env.*, .secrets/, .obsidian/) before the first commit. For GitHub, ask private (suggested) or public, and get my yes before you create the repo or push. Tell me if gh (the GitHub command-line tool) is missing or not logged in.
5. Interview, sized to the project. Ask about goal, audience, done-when, limits (time, money, tools), main risks, and "what command or observation proves this works?" For a small project, three questions and a five-line plan are enough. Stop when you can restate the goal, the done-when, and the first three tasks, and I confirm. Draft in kb/research/plan-draft.md; after my yes, move it to kb/approved/plan.md and add its steps to todo.md. If files already exist, read them and ask only about the gaps.
6. Save as you go. Log each decision I make in kb/approved/decisions.md at once: date, decision, reason. After each task, tick todo.md and update status.md before you reply. When todo.md passes 30 lines, move finished tasks to kb/done.md. Change Last review only when we do the review in rule 9. Do not wait for me to say goodbye. If something cannot be saved, tell me exactly what.
7. Check, then review. Create .claude/agents/reviewer.md now: read-only (tools: Read, Grep, Glob). Run the proof from rule 5 before you call a task done; if there is none yet, ask me for one at the first coding task. Before any code merge, give the reviewer the diff and the plan, never this chat. It reports only problems that break things and skips style. Docs-only changes skip review. Do not change the reviewer's tools.
8. Background agents. Use them only for long, parallel, or clean-context work, because each costs my usage. Each gets a full brief (goal, files, done when), because it cannot see the chat. Say in one line what each is doing, and tell me the result in 3 lines when it finishes. Parallel writers each get their own worktree and branch, plus a PR if we use GitHub, three at most. Two agents never write the same files.
9. Learn. After a mistake, add one dated line with its reason to kb/lessons.md, 20 lines at most. If Last review is over seven days old, prune lessons and propose up to three improvements (a CLAUDE.md line, a skill, a test, or a hook). A lesson that repeats goes into CLAUDE.md or becomes a hook proposal. A task that repeats twice becomes a skill proposal (check official skills first). Propose another agent only when a skill is not enough and we can measure the gain: name, job, tools, why. Max 3, I approve each, do not create them first. Hooks, settings, and permissions change only with my yes.
10. Language. Talk to me in simple English (A2). Keep commands, error text, and technical terms exact. Ask decisions as short cards: one question, two or three options with an example each, your pick, and what changes. Batch the cards.
```

**Change rule 10 to your own language and level** (for example "simple Spanish"). A2 is a basic English level.

**What you should see:** the agent asks about git first, shows you `.claude/settings.json` for approval, then interviews you card by card. When the plan is approved, these files exist: `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/reviewer.md`, `kb/status.md`, `kb/todo.md`, `kb/approved/decisions.md`, `kb/approved/plan.md`.

**Optional:** open the project folder in [Obsidian](https://obsidian.md) to read `CLAUDE.md` and the files in `kb/` as notes.

Start fresh each new day, each new big task, or when the chat gets long or the topic changes: type `/clear` in the current session, or open a **new** session in the project, and say "hello". The state lives in `CLAUDE.md`, `kb/status.md`, and `kb/todo.md`, not in the chat. `/clear` is usually enough. Open a new session instead if the agent just created or changed agents, hooks, or settings, because Claude Code may load those only when a session starts.

### If a session ends

- **Nothing special to do.** The prompt saves as you go: decisions go to `kb/approved/decisions.md` when you make them, and `kb/status.md` and `kb/todo.md` are updated after every finished task. If a window closes or a session crashes, the files are current as of the last finished task, as long as the agent followed rule 6.
- **Want to be sure?** Ask "Is everything saved?" The agent checks `kb/status.md` and `kb/todo.md` and fixes them if needed.
- **Next session:** type `/clear` (or open a new session) and say "hello". `CLAUDE.md` loads `kb/status.md` and `kb/todo.md` by itself, and the agent continues from "Next step".

## What it does, and what it does not

- Most of it is **advice**. The agent can drift from it. The exception is rule 2: the agent writes `.claude/settings.json`, and Claude Code itself then blocks reads of `.env` and asks you before a push, merge, delete, or edit of `kb/approved/plan.md`. Open that file and check it. The agent could not enforce "send, publish, deploy, pay" with settings, so those stay advice.
- The interview is advice too. The agent may stop asking too early. If the plan feels thin, say "interview me more".
- The reviewer is read-only only because of its `tools: Read, Grep, Glob` line. After the agent creates the file, open it and check that line. Nothing stops the agent from editing it later.
- It does not create a check. A new project has no tests on day one, so rule 7 makes the agent ask you for one at the first coding task.
- "Save as you go" is advice too. The agent can forget to update `kb/status.md` or `kb/todo.md`. Ask "Is everything saved?" now and then. To make saving automatic and enforced, you need a hook (a small script that runs by itself), which this prompt-only repo does not include.
- The agent cannot see how full its memory is. Check `/context` yourself, and start a new session (after the agent has saved) before it gets very full.
- It sets up git, but not GitHub branch protection or a usage watch. If you choose "local only", there is no copy of your work on another computer.
- Parallel writers need your review. Each one opens its own PR, and you read and merge them. Two or three at a time is about what one person can review. If two PRs touch the same code, the second one must be updated after the first is merged.
- Background agents spend their own usage, each starts with a fresh memory (it does not see the chat), and their permission questions appear in your main chat. Many at once can use a lot of your limit.
- It has not been tested over weeks of real use. Expect to adjust the wording after a week.
- Claude Code docs: rules with no exceptions belong in settings, not prose, which is why rule 2 writes `.claude/settings.json`. The agent writes the shell rules for each shell tool it has in the session (Bash, PowerShell, or both). The rule formats, such as `Edit(kb/approved/plan.md)`, are not tested here, so try to edit that file once, and try a push, and check that Claude Code asks you. A Stop hook can enforce "run a check before you say done" the same way, but this repo does not include one.

## Why one agent, not many

Anthropic advises starting with one agent loop plus skills and adding agents only when you can measure a gain. Cognition found that one writer plus reviewers works, and parallel writers do not. A CEO, CMO, and CTO agent is the org-chart pattern. So the "agent on top" here is a **role written in files**, and extra agents are proposed, not created, with a limit of three that you approve. Rule 8 uses background agents to keep the chat free for you and to speed up a list of changes: reading and testing run in parallel, and writing runs in parallel only when each agent has its own git worktree, its own branch, and its own files. The rule is "never two writers on the same files", not "one writer in the whole project".

Sources (checked 9 to 12 Nov 2026):

- [Anthropic, "Building agents: When to fold subagents into your main agent loop"](https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
- [Cognition, "Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working)
- [Anthropic, "Prompting best practices"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic, "Prompting Claude Fable 5.2"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- [Claude Code, "Best practices"](https://code.claude.com/docs/en/best-practices)
- [Claude Code, "How Claude remembers your project"](https://code.claude.com/docs/en/memory)
- [Claude Code docs](https://code.claude.com/docs): Skills, Subagents, Hooks

## License

MIT. See [LICENSE](LICENSE). Not affiliated with Anthropic.
