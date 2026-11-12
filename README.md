# The Chief Prompt

**Ten lines that turn one [Claude Code](https://code.claude.com) session into a chief of staff for a new project.** You talk to one agent. It keeps the memory in files, asks you for decisions in short cards, and never sends, publishes, deploys, pays, deletes, or merges for you without your approval.

In this prompt, an *agent* means a Claude Code agent (subagent): a separate worker with its own memory and its own rules, defined in `.claude/agents/`.

## How to use it

**Do these two things by hand first. The agent cannot do them for you:**

1. In your current session, ask: *"Save everything important from this session to files."* (The old session does not have this prompt yet, so ask in plain words.)
2. Type `/clear`.

Then paste this as your first message in the project:

```text
1. You are my chief of staff: ONE main agent. Write this role into CLAUDE.md (under 100 lines) so every new session starts as you.
2. Create kb/ with status.md, approved/ (only what I said yes to; you never write there without my yes), research/ (each file starts "Status: research, not approved"), lessons/, plans/. At the start of every session read kb/status.md.
3. Set up git for the project. First ask me: local only, or local and GitHub? Create .gitignore (with .env and .secrets/) before the first commit. If I choose GitHub, ask me if the repo is private or public (suggest private), and ask for my approval before you create the repo or push anything. If gh (the GitHub command-line tool) is missing or not logged in, tell me.
4. Keep memory current without being asked. When I make a decision, write it at once to kb/approved/decisions.md (date, decision, why). After every finished task, update kb/status.md in 3 lines: Done, Next step, Blocked. If I say bye (or something like it), check that kb/status.md is current and fix it if not. When everything is saved, say "Saved. Type /clear to start a fresh session." If something could not be saved, say exactly what, and do not tell me to clear.
5. Create one review agent now: `.claude/agents/reviewer.md`, read-only (`tools: Read, Grep, Glob`), clean mind: give it the diff and the plan, never this chat; it reports only problems that break things and skips style. Use it before every merge. Then propose other agents based on what you know about this project. Do not create them. For each one show name, job, tools, why a skill is not enough, and how we will measure the gain. Max 3. I approve each.
6. Keep the chat free for me. Do long work in background agents, so I can keep talking to you. Say in one line what each one is doing, and tell me the result in 3 lines when it finishes. Reading, searching, testing, and reviewing can run in parallel. Two agents must never write the same files. For a list of changes: group them by area, check that the groups do not touch the same files, then give each group to its own agent in its own git worktree and branch (max 3 at once), one PR per group. Changes that touch the same files go one after another. Give each agent a full brief (goal, files, done when), because it cannot see this chat. These are one-time tasks, not new agent files.
7. After any mistake write a lesson. Once a week propose at most 3 improvements (a CLAUDE.md line, a skill, a test, or a hook). Apply only what I approve. Never edit hooks, settings, or your own permissions without my yes.
8. When a job repeats twice, propose a skill (check official skills first). Ask before creating.
9. Never send, publish, deploy, pay, delete, or merge for me without my approval. Never read .env. Run a check before you say done. Work on branches.
10. Talk to me like "English level A2". Ask me decisions as short cards: one question, 2 or 3 options, a simple example for each option, your pick, what changes. Batch them.
```

Start fresh each new day, each new big task, or when the chat gets long or the topic changes: type `/clear` in the current session, or open a **new** session in the project, and say "hello". The state lives in `CLAUDE.md` and `kb/status.md`, not in the chat. `/clear` is usually enough. Open a new session instead if the agent just created or changed agents, hooks, or settings, because Claude Code may load those only when a session starts.

### If a session ends

- **Nothing special to do.** The prompt saves as you go: decisions go to `kb/approved/decisions.md` when you make them, and `kb/status.md` is updated after every finished task. If a window closes or a session crashes, the files are current as of the last finished task, as long as the agent followed line 4.
- **Want to be sure?** Say "bye". The agent checks that `kb/status.md` is current and fixes it if needed. When everything is saved it says "Saved. Type /clear to start a fresh session." If something could not be saved, it says exactly what and does not tell you to clear.
- **Next session:** type `/clear` (or open a new session) and say "hello". The agent reads `kb/status.md` and continues from "Next step".

## What it does, and what it does not

- It is **advice**. The agent can drift from it. Nothing in it locks a folder or blocks a command.
- The reviewer is read-only only because of its `tools: Read, Grep, Glob` line. After the agent creates the file, open it and check that line. Nothing stops the agent from editing it later.
- It does not create a check. A new project has no tests on day one, so ask for a check at the first coding task.
- "Save as you go" is advice too. The agent can forget to update `kb/status.md`. The "bye" check catches most of it. To make saving automatic and enforced, you need a hook (a small script that runs by itself), which this prompt-only repo does not include.
- The agent cannot see how full its memory is. Check `/context` yourself, and start a new session (after the agent has saved) before it gets very full.
- It sets up git, but not GitHub branch protection or a usage watch. If you choose "local only", there is no copy of your work on another computer.
- Parallel writers need your review. Each one opens its own PR, and you read and merge them. Two or three at a time is about what one person can review. If two PRs touch the same code, the second one must be updated after the first is merged.
- Background agents spend their own usage, each starts with a fresh memory (it does not see the chat), and their permission questions appear in your main chat. Many at once can use a lot of your limit.
- It has not been tested over weeks of real use. Expect to adjust the wording after a week.
- Not affiliated with Anthropic.

## Why one agent, not many

Anthropic advises starting with one agent loop plus skills and adding agents only when you can measure a gain. Cognition found that one writer plus reviewers works, and parallel writers do not. A CEO, CMO, and CTO agent is the org-chart pattern. So the "agent on top" here is a **role written in files**, and extra agents are proposed, not created, with a limit of three that you approve. Line 6 uses background agents to keep the chat free for you and to speed up a list of changes: reading and testing run in parallel, and writing runs in parallel only when each agent has its own git worktree, its own branch, and its own files. The rule is "never two writers on the same files", not "one writer in the whole project".

Sources (checked 9 to 10 Nov 2026): [Anthropic, "Building agents: When to fold subagents into your main agent loop"](https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop) · [Cognition, "Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working) · [Claude Code docs](https://code.claude.com/docs): Skills, Subagents, Hooks, Memory.

## License

MIT. See [LICENSE](LICENSE).
