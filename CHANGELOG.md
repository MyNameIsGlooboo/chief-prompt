# Changelog

The newest change is first. The numbers are pull requests in this repo.

## 2026-11-14

- Five small edits from the prompt audit (`/doctor prompt-audit template`). A search, and opening or reading a page, is not "sending", so the agent does not ask before it (rules file and autopilot skill). A background agent's result comes in a few lines, not in exactly three, and names what it could not check. The reviewer names what it could not check after "No blocking problems". The reviewer also works from the goal of the change when the plan does not cover it. The rule against `;` in the ship command now gives its reason.
- `.claude/settings.json` has four allow rules: `mcp__claude-in-chrome__*`, `mcp__Claude_Browser__*`, `WebFetch` and `WebSearch`. Claude Code no longer asks before the agent browses, clicks, or runs JavaScript in a page. The install and the update add them to a settings file that already exists. Read the new point in [docs/limits.md](docs/limits.md) first: your own Chrome has your logins.
- The ship step runs as one joined command (push, PR, checks, merge, branch delete), so Claude Code asks once and not for each part. Reason: the ask rules also ask in bypass mode, and the session logs of this repo showed 53 push and 29 merge commands that each matched an ask rule.

## 2026-11-13

- Second sources review, three changes. The install keeps a project's `AGENTS.md` alive: it adds `@AGENTS.md` to a new `CLAUDE.md`, and the install and the update ask first when `CLAUDE.md` already existed. The autopilot warning names the setting `denyInsteadOfPrompting`. The reviewer starts without `CLAUDE.md` and the rules file (`omitClaudeMd: true`).
- A second install line in `README.md`, for a project that already has files. The agent stops if there is no git repo or if work is not committed, and it replaces none of your own files. The steps are the same `template/SETUP.md`.
- One-line update. `README.md` shows an update line to paste, like the install line. The agent reads the newest update steps from the clone, so one run is enough and the project needs no update skill. `/chief-update` still works.
- `README.md` has its own "Autopilot" section, with a diagram and the steps to use it. The check script now allows 140 lines and 4 diagrams.
- Add the autopilot skill to the template: type `/chief-autopilot`. Local only, one `autopilot` branch, no push, no merge, no delete.
- `README.md` is short now and has three diagrams. The long parts moved to `docs/`: the guide, all limits, "Why one agent", and the maintainer part.
- One-line install. The five steps moved to `template/SETUP.md`, and `README.md` shows one line to paste.
- Add this changelog and the "Last updated" line at the top of `README.md`. The check script checks both.
- Add an update skill to the template: type `/chief-update` in a project (#8).
- Split the template. The rules live in `.claude/rules/chief-of-staff.md`, and the prompt no longer replaces a project's own files (#7).
- One approval now covers the whole ship step: push, PR, merge, and delete of the merged branch (#6).
- The sources review is now a skill, for this repo only (#5).
- First sources review. The approval rule is exact about "sending", and two notes in `README.md` are up to date (#4).
- Add a sources review to the "Learn" step: `kb/sources.md` (#3).
- This repo now uses its own prompt (#2).
- Ship the rules as files in `template/`, add the check script, and make the prompt shorter (#1).
- Rewrite the rules: settings that Claude Code enforces, imports of the `kb/` files, and an interview sized to the project.

## 2026-11-12

- First version of the prompt.
- Add the interview step, `kb/todo.md`, and the tip to block reads of `.env`.
- Tighten the rules after a review of the prompting docs, and list the sources.
