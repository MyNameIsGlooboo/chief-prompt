# Changelog

The newest change is first. The numbers are pull requests in this repo.

## 2026-11-13

- A second install line in `README.md`, for a project that already has files. The agent checks `git status` first and replaces none of your files. The steps are the same `template/SETUP.md`.
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
