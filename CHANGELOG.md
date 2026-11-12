# Changelog

The newest change is first. The numbers are pull requests in this repo.

## 2026-11-13

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
