Status: research, not approved

# Autopilot questions, run of 2026-11-13

The owner started the run with two new tasks. They are the last two lines of `kb/todo.md`.

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
