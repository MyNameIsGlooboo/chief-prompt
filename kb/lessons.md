# Lessons

One dated line per mistake, with its reason. 20 lines at most.
- 2026-11-13: Code written into `scripts/check.py` from a Python script inside a Bash heredoc broke twice: each backslash-n in a string became a real line break. Reason: the escape was read one time too many. Write code that has backslashes with the Edit tool.
- 2026-11-13: `git commit -m` with a here-string in PowerShell failed on a message with double quotes. Reason: PowerShell 5.1 splits the argument at the quotes. Use Bash with `git commit -F -` and a heredoc.
- 2026-11-13: The autopilot design named option branches `autopilot/q1-b`, and git refuses that name while a branch `autopilot` exists. Reason: the git commands were written from memory and not run. Try each git command of a new skill in a test repo before the review.
- 2026-11-13: A commit went in while `python scripts/check.py` failed (`template/SETUP.md` had 401 words). Reason: the check and `git commit` were joined with `;`, so the commit ran after the failure. Join the check and the commit with `&&`.
- 2026-11-14: The owner asked why Claude Code asks so often, and the agent answered with a guess (the delete rule). The session logs showed the push and merge rules: 82 of 88 commands. Reason: the agent did not look at the logs before it answered. For a question about what happened in past sessions, count in the session logs first.
- 2026-11-14: The "About" text of the GitHub repo said "Ten lines" and "for a new project" long after both were wrong (PR 7 and PR 10). The owner found it, not the agent. Reason: the text is on GitHub and not in a file, so no rule and no check read it. Root `CLAUDE.md` now says to check it when the first line of `README.md` changes.
