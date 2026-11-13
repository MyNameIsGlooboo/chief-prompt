Status: research, not approved

# Autopilot questions, run of 2026-11-13

The owner started the run with two new tasks. They are the last two lines of `kb/todo.md`.

## Report

- Tasks done (2): the "Autopilot" section in `README.md` with a diagram and five steps, and the one-line update. `python scripts/check.py` passes after each one.
- Tasks blocked: none.
- Tasks skipped (4): the four "try it in a real project" tasks. They need changes outside this folder.
- Stashes: none.
- Option branches: none.
- Files to delete: none.
- Open questions (2): the README limit (now 140 lines, 4 diagrams), and what the "one line" for the update is. See below.
- Not done on purpose: no push, no merge, no reviewer yet. `scripts/check.py` and the update skill changed, so the reviewer must read the diff before the merge.
- Not tested: the update line in a real project. The mermaid diagram was not rendered on GitHub.
- Small point: root `CLAUDE.md` still says the product is "the one line". There are two lines now.

## Notes

- Skipped: "Try the prompt in one project that already has a `CLAUDE.md`...". Reason: it needs changes in another project folder, and autopilot never changes anything outside this folder.
- Skipped: "Try `/chief-update` in one project after the next template change". Same reason.
- Skipped: "Use the prompt in one real project". Same reason.
- Skipped: "Try `/chief-autopilot` in one real project with three small tasks". Same reason.

### Question 1: `README.md` is too short for a new section

The check script allows 100 lines and exactly 3 diagrams. `README.md` had 97 lines. An autopilot section with a diagram and the steps needs about 20 lines, and the update line needs some more.

- Option a (my pick): raise the limit to 140 lines and 4 diagrams, in `scripts/check.py` and in the rule in root `CLAUDE.md`.
- Option b: keep 100 lines. Then the "Who decides" diagram or the "Five limits" part must move to `docs/`.
- Reason for my pick: you asked for the section in the README, and you picked the other parts of the README yourself in PR 11. I did not want to remove one of them without you.
- Option b is not built.

### Question 2: what is the "one line" for the update?

The update was already one command, `/chief-update`. But it was not as simple as the install: a project with no skill had to paste the install line first, and a project with an old skill had to run the update two times in two sessions.

- Option a (my pick): one update line to paste, like the install line. The agent clones the repo and reads the newest `template/.claude/skills/chief-update/SKILL.md` from the clone. So the steps are always the newest, one run is enough, and it works in a project that has no update skill. `/chief-update` stays as a second way.
- Option b: the same line, and remove the update skill from the template, so there is only one way. Then the steps move to a new file `template/UPDATE.md`. This deletes a template file, and old projects keep a dead skill.
- Option c: change nothing, because `/chief-update` is already one line.
- Reason for my pick: it is the same pattern as the install, it removes the "run it twice" case, and it deletes nothing.
- Option b is not built: it needs a delete, and autopilot never deletes.
- The check script now wants exactly two blocks to paste in `README.md`: the install line and the update line.
