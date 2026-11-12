# The Chief Prompt

**One short prompt and four ready files that turn one [Claude Code](https://code.claude.com) session into a chief of staff for a new project.** You talk to one agent. It interviews you until it can write a plan, keeps the memory in files, asks you for decisions in short cards, and never sends, publishes, deploys, pays, deletes, or merges for you without your approval.

In this prompt, an *agent* means a Claude Code agent (subagent): a separate worker with its own memory and its own rules, defined in `.claude/agents/`.

**Why it is short:** there are many guides on this topic, so this repo collects them in one place. The prompt stays short and gives the agent few instructions and no skills to start with. It does not depend on how smart a model is, so it should need fewer updates when models get stronger or weaker. Models change, so re-check it from time to time.

## How to use it

**Brand-new empty folder?** Skip to the paste step.

**Already talked in a session about this project?** Do these two things by hand first. The agent cannot do them for you:

1. In your current session, ask: *"Save everything important from this session to files."* (The old session does not have this prompt yet, so ask in plain words.)
2. Type `/clear`.

Then paste this as your first message in the project:

```text
Do these steps in order.
1. Setup files. Copy CLAUDE.md, .gitignore, .claude/settings.json and .claude/agents/reviewer.md from the template/ folder of https://github.com/MyNameIsGlooboo/chief-prompt into this folder: clone the repo to a temporary folder, copy the four files, then remove the clone. Copy them exactly and do not rewrite them. If one of these files already exists here, or git is missing, stop and ask me. Show me .claude/settings.json and wait for my yes before the first commit. CLAUDE.md is now your rules for this project: you are my chief of staff, one main agent, no team.
2. Language. Set the Language line in CLAUDE.md to: simple English (A2). Talk to me that way from now on.
3. Memory folder. Create kb/ as CLAUDE.md describes: status.md, todo.md, done.md, lessons.md, approved/ and research/. Set Last review in status.md to today's date.
4. Git. Ask me: local only, or GitHub too? For GitHub, ask private (suggested) or public, and get my yes before you create the repo or push. Tell me if gh (the GitHub command-line tool) is missing or not logged in.
5. Interview, sized to the project. Ask about goal, audience, done-when, limits (time, money, tools), main risks, and "what command or observation proves this works?" For a small project, three questions and a five-line plan are enough. Stop when you can restate the goal, the done-when, and the first three tasks, and I confirm. Draft in kb/research/plan-draft.md; after my yes, write it to kb/approved/plan.md and add its steps to todo.md. If files already exist, read them and ask only about the gaps.
```

**Change step 2 to your own language and level** (for example "simple Spanish"). A2 is a basic English level.

**What the prompt copies:** four files from the [`template/`](template) folder of this repo. The agent copies them and does not write them itself, so every project gets the same rules:

- [`CLAUDE.md`](template/CLAUDE.md): the standing rules, loaded in every session.
- [`.claude/settings.json`](template/.claude/settings.json): the rules that Claude Code itself enforces.
- [`.claude/agents/reviewer.md`](template/.claude/agents/reviewer.md): the read-only reviewer.
- [`.gitignore`](template/.gitignore)

You can also copy the four files into your project by hand before you paste the prompt. Then the agent skips the copy.

**What you should see:** the agent copies the four files, shows you `.claude/settings.json` for approval, asks about git, then interviews you card by card. When the plan is approved, these files exist: `CLAUDE.md`, `.gitignore`, `.claude/settings.json`, `.claude/agents/reviewer.md`, `kb/status.md`, `kb/todo.md`, `kb/approved/decisions.md`, `kb/approved/plan.md`. Then open a new session, so Claude Code loads the new settings and the reviewer.

**Optional:** open the project folder in [Obsidian](https://obsidian.md) to read `CLAUDE.md` and the files in `kb/` as notes.

Start fresh each new day, each new big task, or when the chat gets long or the topic changes: type `/clear` in the current session, or open a **new** session in the project, and say "hello". The state lives in `CLAUDE.md`, `kb/status.md`, and `kb/todo.md`, not in the chat. `/clear` is usually enough. Open a new session instead if the agent just created or changed agents, hooks, or settings, because Claude Code may load those only when a session starts.

### If a session ends

- **Nothing special to do.** The prompt saves as you go: decisions go to `kb/approved/decisions.md` when you make them, and `kb/status.md` and `kb/todo.md` are updated after every finished task. If a window closes or a session crashes, the files are current as of the last finished task, as long as the agent followed the "Save as you go" rules in `CLAUDE.md`.
- **Want to be sure?** Ask "Is everything saved?" The agent checks `kb/status.md` and `kb/todo.md` and fixes them if needed.
- **Next session:** type `/clear` (or open a new session) and say "hello". `CLAUDE.md` loads `kb/status.md` and `kb/todo.md` by itself, and the agent continues from "Next step".

## What it does, and what it does not

- Most of it is **advice**. The agent can drift from it. The exception is `.claude/settings.json`: Claude Code itself blocks reads of `.env`, `.env.*` and `.secrets/`, and asks you before a push, a merge, a delete, or an edit of `kb/approved/plan.md`. Settings cannot enforce "ask before sending email or messages to other people, publishing, deploying, or paying", so that stays advice. "Sending" means to other people. A reply to you or a brief to a background agent needs no approval.
- The settings have limits. The read block covers Claude's file tools and shell commands that Claude Code knows, such as `cat`. It does not cover a script that opens the file itself. The delete rule matches `rm` and `Remove-Item`, not every other way to delete a file. For a block on every process, turn on the Claude Code sandbox.
- The interview is advice too. The agent may stop asking too early. If the plan feels thin, say "interview me more".
- The reviewer is read-only only because of its `tools: Read, Grep, Glob` line. Nothing stops the agent from editing that file later.
- It does not create a check. A new project has no tests on day one, so `CLAUDE.md` makes the agent ask you for one at the first coding task.
- "Save as you go" is advice too. The agent can forget to update `kb/status.md` or `kb/todo.md`. Ask "Is everything saved?" now and then. To make saving automatic and enforced, you need a hook (a small script that runs by itself), which this prompt-only repo does not include.
- Long chats cost more and lose focus. Type `/clear` between tasks (after the agent has saved). You rarely run out of memory now, because Claude Code makes the chat shorter by itself.
- It sets up git, but not GitHub branch protection or a usage watch. If you choose "local only", there is no copy of your work on another computer.
- Parallel writers need your review. Each one opens its own PR, and you read and merge them. Two or three at a time is about what one person can review. If two PRs touch the same code, the second one must be updated after the first is merged.
- Background agents spend their own usage, each starts with a fresh memory (it does not see the chat), and their permission questions appear in your main chat. Many at once can use a lot of your limit.
- It has not been tested over weeks of real use. Expect to adjust the wording after a week.
- Claude Code docs: rules with no exceptions belong in settings, not prose, which is why this repo ships `.claude/settings.json`. It has the shell rules for both Bash and PowerShell. The rule formats follow the [permissions docs](https://code.claude.com/docs/en/permissions) (checked 13 Nov 2026), and a script checks that every rule is in the file. They are not tested in a live session, so try to edit `kb/approved/plan.md` once, and try a push, and check that Claude Code asks you. A Stop hook can enforce "run a check before you say done" the same way, but this repo does not include one.

## Why one agent, not many

Anthropic advises starting with one agent loop plus skills and adding agents only when you can measure a gain. Cognition found that one writer plus reviewers works, and parallel writers do not. A CEO, CMO, and CTO agent is the org-chart pattern. So the "agent on top" here is a **role written in files**, and extra agents are proposed, not created, with a limit of three that you approve. `CLAUDE.md` uses background agents to keep the chat free for you and to speed up a list of changes: reading and testing run in parallel, and writing runs in parallel only when each agent has its own git worktree, its own branch, and its own files. The rule is "never two writers on the same files", not "one writer in the whole project".

Sources (checked 9 to 12 Nov 2026):

- [Anthropic, "Building agents: When to fold subagents into your main agent loop"](https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
- [Cognition, "Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working)
- [Anthropic, "Prompting best practices"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic, "Prompting Claude Fable 5.2"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- [Claude Code, "Best practices"](https://code.claude.com/docs/en/best-practices)
- [Claude Code, "How Claude remembers your project"](https://code.claude.com/docs/en/memory)
- [Claude Code docs](https://code.claude.com/docs): Skills, Subagents, Hooks

## For the maintainer only

This part is for the owner of this repo. If you only use the prompt, skip it.

**Check.** `python scripts/check.py` checks the template files and the prompt: valid JSON, every deny and ask rule present for Bash and PowerShell, the reviewer's tools line, `CLAUDE.md` under 100 lines with both imports, the prompt under 400 words, and the root copies equal to the template. It uses no model and costs nothing. GitHub Actions runs it on every push and pull request.

**This repo uses its own prompt.** The root `CLAUDE.md` imports `template/CLAUDE.md` and adds a few rules for this repo. The root `.claude/settings.json`, `.claude/agents/reviewer.md` and `.gitignore` are exact copies of the template files, and the check script fails if they differ. The `kb/` folder holds this repo's own status, tasks, and decisions.

**Feedback from my own projects.** This is only for me. It is not in the template, and other users do not need it. In my own projects I add this line to the "Learn" part of `CLAUDE.md`:

```markdown
- If a rule in this file fails or confuses you, add a dated line to kb/chief-prompt-lessons.md: the rule, what happened, and why. Never prune this file.
```

This file is separate from `kb/lessons.md`. `kb/lessons.md` is about the project, has a 20-line limit, and gets pruned. `kb/chief-prompt-lessons.md` is about this prompt and keeps every line.

Before I update this repo, I collect `kb/chief-prompt-lessons.md` from my projects. The lines show which rules fail in real use.

**Keeping it up to date.** [`kb/sources.md`](kb/sources.md) lists the trusted pages. At each review (when Last review is over seven days old), the agent reads them, compares them with `template/` and `README.md`, and writes what it finds to `kb/research/`. It proposes three changes at most, and I approve each one. This is advice, not enforced: it runs only when I open a session in this repo.

## License

MIT. See [LICENSE](LICENSE). Not affiliated with Anthropic.
