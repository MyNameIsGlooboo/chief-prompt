---
name: sources-review
description: Compare the trusted pages in kb/sources.md with template/ and README.md, and write the findings to kb/research/. Use at each "Learn" review in this repo, or when the owner asks if the prompt is still up to date.
---

Check that the prompt still agrees with its sources. Write findings and proposals only. Do not edit `template/` or `README.md` in this skill.

## Steps

1. Work on a new branch. Read `kb/sources.md` for the page list, and the newest file in `kb/research/` named `sources-*.md` for what the last review found and what it left unread.
2. Fetch each page into a temporary folder outside the repo. Claude Code and Anthropic docs pages also exist as Markdown: add `.md` to the URL. That version is much smaller than the HTML. A page that does not answer goes into the report as "not reachable".
3. Do not read every page in full. List the headings first, then read the parts that touch a rule. The changelog is over 1 MB: search it for `permission rule`, `deny rule`, `ask rule`, `CLAUDE.md`, `subagent`, and `skill`, and read only the lines found.
4. Compare, file by file:
   - `template/.claude/settings.json` with the Permissions page: rule syntax, the Bash and PowerShell parts, and how `Read` and `Edit` path patterns match.
   - `template/.claude/agents/reviewer.md` with the frontmatter reference on the Subagents page.
   - `template/.claude/rules/chief-of-staff.md` and `template/CLAUDE.md` with the Memory page (size, imports, `.claude/rules/`) and with the newest "Prompting Claude ..." guide (approval wording, subagents, cautions that pile up).
   - `README.md`, part "What it does, and what it does not", with Best practices, most of all its part "What you can stop doing".
   - The engineering blog: read the titles, and open a post only if it is about agent memory, subagents, or instruction files.
5. Ask the owner to run `/doctor prompt-audit template`, because only the owner can type it. Add its findings to the report. If the owner skips it, say so in the report.
6. Write `kb/research/sources-YYYY-MM-DD.md` with today's date. The first line is "Status: research, not approved". Use these parts, in this order:
   - Short result: is any rule broken, yes or no.
   - What was read: a table with each page and how much of it was read. Be honest about pages read in part or not at all.
   - What matches: no change needed.
   - Proposals: three at most. Each one names the source and its part, the rule it changes, why, a possible wording, and the cost.
   - Smaller notes: things seen that are not worth a proposal.
7. Set "Last read" in `kb/sources.md` to today's date. Update `kb/todo.md` and `kb/status.md`. Run `python scripts/check.py` and commit.
8. Show the owner the proposals as cards. Stop here and wait.

## After the owner decides

- Log each yes or no in `kb/approved/decisions.md`.
- A change in `template/` counts as code: give the `reviewer` agent the diff and the approved proposal before the merge.
- When a rule changes, update "What it does, and what it does not" in `README.md` in the same change.

## Limits

- Only the owner adds a page to `kb/sources.md`. If a new page looks useful, name it under "Smaller notes".
- State as fact only what a page says. Mark anything you inferred as "not tested".
