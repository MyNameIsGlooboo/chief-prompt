# Guide

The details behind the short [README](../README.md).

In this prompt, an *agent* means a Claude Code agent (subagent): a separate worker with its own memory and its own rules, defined in `.claude/agents/`.

## Before you paste the line

**Brand-new empty folder?** Paste the line from the README.

**Already talked in a session about this project?** Do these two things by hand first. The agent cannot do them for you:

1. In your current session, ask: *"Save everything important from this session to files."* (The old session does not have this prompt yet, so ask in plain words.)
2. Type `/clear`.

**Project that already has files?** The prompt replaces none of your files. It adds three files of its own, `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md` and `.claude/skills/chief-autopilot/SKILL.md`, and adds only the missing lines to your `CLAUDE.md`, `.gitignore` and `.claude/settings.json`. The [README](../README.md#start) has a second line for this case. It makes the agent stop if the folder is not a git repo or if `git status` shows work that is not committed, so `git diff` shows you what was added. If your project has an `AGENTS.md`, the agent adds the line `@AGENTS.md` to a new `CLAUDE.md`, because Claude Code reads only `CLAUDE.md` when both files exist:

```text
This project already has files. If this folder is not a git repo, stop and ask me to run git init and commit my files first. Then run git status, and if it shows work that is not committed, stop and ask me to commit it. Then clone https://github.com/MyNameIsGlooboo/chief-prompt to a temporary folder outside this project, read its template/SETUP.md, and do the steps in it. Replace none of my own files. My language: simple English (A2).
```

Paste your line as your first message in the project.

**The steps are in [`template/SETUP.md`](../template/SETUP.md):** setup files, language, memory folder, git, interview. The agent reads them from this repo, so you paste one line and not five steps. Read the file first if you want to know what the agent will do.

## What the agent copies

Seven files from the [`template/`](../template) folder of this repo. The agent does not write them itself, so every project gets the same rules. The eighth file in that folder, `SETUP.md`, holds the steps. The agent does not copy it.

Three files belong to the prompt. The agent copies them exactly, and an update replaces them:

- [`.claude/rules/chief-of-staff.md`](../template/.claude/rules/chief-of-staff.md): the standing rules. Claude Code loads every file in `.claude/rules/` in every session.
- [`.claude/skills/chief-update/SKILL.md`](../template/.claude/skills/chief-update/SKILL.md): the update skill. It runs only when you type `/chief-update`.
- [`.claude/skills/chief-autopilot/SKILL.md`](../template/.claude/skills/chief-autopilot/SKILL.md): the autopilot skill. It runs only when you type `/chief-autopilot`.

Four files belong to you. The agent copies one only if you do not have it. If you have it, the agent adds the missing lines and changes nothing else:

- [`CLAUDE.md`](../template/CLAUDE.md): the rules of your project. The prompt needs only the Language part and two import lines in it.
- [`.claude/settings.json`](../template/.claude/settings.json): the rules that Claude Code itself enforces.
- [`.claude/agents/reviewer.md`](../template/.claude/agents/reviewer.md): the read-only reviewer.
- [`.gitignore`](../template/.gitignore)

You can also copy the seven files into an empty project by hand before you paste the line. Then the agent finds nothing to add.

## What you should see

The agent copies or completes the seven files, tells you what it added, shows you `.claude/settings.json` for approval, asks about git, then interviews you card by card. When the plan is approved, these files exist: `CLAUDE.md`, `.gitignore`, `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md`, `.claude/skills/chief-autopilot/SKILL.md`, `.claude/settings.json`, `.claude/agents/reviewer.md`, `kb/status.md`, `kb/todo.md`, `kb/approved/decisions.md`, `kb/approved/plan.md`. Then open a new session, so Claude Code loads the new settings and the reviewer.

**Optional:** open the project folder in [Obsidian](https://obsidian.md) to read `CLAUDE.md` and the files in `kb/` as notes.

## Each new day

Start fresh each new day, each new big task, or when the chat gets long or the topic changes: type `/clear` in the current session, or open a **new** session in the project, and say "hello". The state lives in `CLAUDE.md`, `kb/status.md`, and `kb/todo.md`, not in the chat. `/clear` is usually enough. Open a new session instead if the agent just created or changed agents, hooks, or settings, because Claude Code may load those only when a session starts.

## Update a project to a newer version of the prompt

Commit your work, then paste the update line from the [README](../README.md#update) in the project. It is one line, like the install:

```text
Clone https://github.com/MyNameIsGlooboo/chief-prompt to a temporary folder outside this project, read its template/.claude/skills/chief-update/SKILL.md, and do the steps in it.
```

The agent reads the newest update steps from this repo and replaces the three files the prompt owns: the rules file, the autopilot skill, and the update skill. In your own files it adds only what is missing: new allow, deny and ask rules in `.claude/settings.json`, new lines in `.gitignore`. If the reviewer file differs, it asks you which one to keep. Then it shows you `git diff` and waits for your yes before it commits. Open a new session after that.

**The line works in every project.** It needs no update skill in the project, and one run is enough, because the steps come from this repo and not from your older copy.

**`/chief-update` is the second way.** It runs the copy of the steps in your project. If that copy is older, the agent tells you to type `/chief-update` once more in a new session.

**Project set up with the first version of the prompt?** There the rules are still inside `CLAUDE.md`, and there is no `.claude/rules/` folder. Paste the line again. The agent adds the rules file, then shows you the old chief-of-staff parts in `CLAUDE.md` and asks before it removes them. Your Language line, your own rules and the two `@kb` lines stay. Do not skip this: if both copies stay, they will disagree after the next update.

## If a session ends

- **Nothing special to do.** The prompt saves as you go: decisions go to `kb/approved/decisions.md` when you make them, and `kb/status.md` and `kb/todo.md` are updated after every finished task. If a window closes or a session crashes, the files are current as of the last finished task, as long as the agent followed the "Save as you go" rules.
- **Want to be sure?** Ask "Is everything saved?" The agent checks `kb/status.md` and `kb/todo.md` and fixes them if needed.
- **Next session:** type `/clear` (or open a new session) and say "hello". `CLAUDE.md` loads `kb/status.md` and `kb/todo.md` by itself, and the agent continues from "Next step".

## Autopilot

Autopilot is a mode that you turn on. It is never on by itself. Type `/chief-autopilot` when `kb/todo.md` has open tasks and you want the agent to work while you are away.

- The agent creates a local branch named `autopilot` and works through the open tasks in order, one commit per task, plus small commits for its notes.
- It does not push, merge, delete files, or change the approved plan. It does not send, publish, deploy, or pay. A task that needs one of these is skipped and listed.
- At an open question it takes its own pick and writes the question to `kb/research/autopilot-questions.md`. It builds another option only when that is small, on its own branch, for example `autopilot-q1-b`.
- If the check for a task fails twice, the agent puts that work into a named `git stash` and goes to the next task. Failed work gets no commit.
- When you are back, say "hello", also in a new session. `kb/status.md` points the agent to the questions file. The agent shows you the report and asks one card per question. Then the `autopilot` branch goes through the normal step: check, reviewer, your one yes.

**Before you start it:** a permission question from Claude Code stops the run until you answer. Auto mode asks the fewest questions ([permission modes](https://code.claude.com/docs/en/permission-modes), checked 13 Nov 2026). The ask rules in `.claude/settings.json` ask in every mode, which is why autopilot never pushes, merges, or deletes. With the setting `denyInsteadOfPrompting`, Claude Code refuses such an action and the run goes on. Only you can set it, and you must turn it off again before you say yes to a branch: see [limits.md](limits.md). Read the limits in [limits.md](limits.md) too.
