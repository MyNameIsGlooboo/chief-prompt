# Lessons

One dated line per mistake, with its reason. 20 lines at most.
- 2026-11-13: Code written into `scripts/check.py` from a Python script inside a Bash heredoc broke twice: each backslash-n in a string became a real line break. Reason: the escape was read one time too many. Write code that has backslashes with the Edit tool.
- 2026-11-13: `git commit -m` with a here-string in PowerShell failed on a message with double quotes. Reason: PowerShell 5.1 splits the argument at the quotes. Use Bash with `git commit -F -` and a heredoc.
