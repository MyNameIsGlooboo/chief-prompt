# Guide

The details behind the short [README](../README.md).

In this prompt, an *agent* means a Claude Code agent (subagent): a separate worker with its own memory and its own rules, defined in `.claude/agents/`.

## Before you paste the line

**Brand-new empty folder?** Paste the line from the README.

**Already talked in a session about this project?** Do these two things by hand first. The agent cannot do them for you:

1. In your current session, ask: *"Save everything important from this session to files."* (The old session does not have this prompt yet, so ask in plain words.)
2. Type `/clear`.

**Project that already has files?** The prompt replaces none of your files. It adds two files of its own, `.claude/rules/chief-of-staff.md` and `.claude/skills/chief-update/SKILL.md`, and adds only the missing lines to your `CLAUDE.md`, `.gitignore` and `.claude/settings.json`. Commit your work first, so `git diff` shows you what was added.

Then paste the line from the [README](../README.md) as your first message in the project.

**The steps are in [`template/SETUP.md`](../template/SETUP.md):** setup files, language, memory folder, git, interview. The agent reads them from this repo, so you paste one line and not five steps. Read the file first if you want to know what the agent will do.

## What the agent copies

Six files from the [`template/`](../template) folder of this repo. The agent does not write them itself, so every project gets the same rules. The seventh file in that folder, `SETUP.md`, holds the steps. The agent does not copy it.

Two files belong to the prompt. The agent copies them exactly, and an update replaces them:

- [`.claude/rules/chief-of-staff.md`](../template/.claude/rules/chief-of-staff.md): the standing rules. Claude Code loads every file in `.claude/rules/` in every session.
- [`.claude/skills/chief-update/SKILL.md`](../template/.claude/skills/chief-update/SKILL.md): the update skill. It runs only when you type `/chief-update`.

Four files belong to you. The agent copies one only if you do not have it. If you have it, the agent adds the missing lines and changes nothing else:

- [`CLAUDE.md`](../template/CLAUDE.md): the rules of your project. The prompt needs only the Language part and two import lines in it.
- [`.claude/settings.json`](../template/.claude/settings.json): the rules that Claude Code itself enforces.
- [`.claude/agents/reviewer.md`](../template/.claude/agents/reviewer.md): the read-only reviewer.
- [`.gitignore`](../template/.gitignore)

You can also copy the six files into an empty project by hand before you paste the line. Then the agent finds nothing to add.

## What you should see

The agent copies or completes the six files, tells you what it added, shows you `.claude/settings.json` for approval, asks about git, then interviews you card by card. When the plan is approved, these files exist: `CLAUDE.md`, `.gitignore`, `.claude/rules/chief-of-staff.md`, `.claude/skills/chief-update/SKILL.md`, `.claude/settings.json`, `.claude/agents/reviewer.md`, `kb/status.md`, `kb/todo.md`, `kb/approved/decisions.md`, `kb/approved/plan.md`. Then open a new session, so Claude Code loads the new settings and the reviewer.

**Optional:** open the project folder in [Obsidian](https://obsidian.md) to read `CLAUDE.md` and the files in `kb/` as notes.

## Each new day

Start fresh each new day, each new big task, or when the chat gets long or the topic changes: type `/clear` in the current session, or open a **new** session in the project, and say "hello". The state lives in `CLAUDE.md`, `kb/status.md`, and `kb/todo.md`, not in the chat. `/clear` is usually enough. Open a new session instead if the agent just created or changed agents, hooks, or settings, because Claude Code may load those only when a session starts.

## Update a project to a newer version of the prompt

Type `/chief-update` in the project. The skill gets the newest `template/` from this repo and replaces the two files the prompt owns: the rules file and the skill itself. In your own files it adds only what is missing: new deny and ask rules in `.claude/settings.json`, new lines in `.gitignore`. If the reviewer file differs, it asks you which one to keep. Then it shows you `git diff` and waits for your yes before it commits. Open a new session after that.

**No `/chief-update` in your project yet?** Paste the line again once. It adds the skill.

**Project set up with the first version of the prompt?** There the rules are still inside `CLAUDE.md`, and there is no `.claude/rules/` folder. Paste the line again. The agent adds the rules file, then shows you the old chief-of-staff parts in `CLAUDE.md` and asks before it removes them. Your Language line, your own rules and the two `@kb` lines stay. Do not skip this: if both copies stay, they will disagree after the next update.

## If a session ends

- **Nothing special to do.** The prompt saves as you go: decisions go to `kb/approved/decisions.md` when you make them, and `kb/status.md` and `kb/todo.md` are updated after every finished task. If a window closes or a session crashes, the files are current as of the last finished task, as long as the agent followed the "Save as you go" rules.
- **Want to be sure?** Ask "Is everything saved?" The agent checks `kb/status.md` and `kb/todo.md` and fixes them if needed.
- **Next session:** type `/clear` (or open a new session) and say "hello". `CLAUDE.md` loads `kb/status.md` and `kb/todo.md` by itself, and the agent continues from "Next step".
