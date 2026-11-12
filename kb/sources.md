# Sources

The trusted pages for this prompt. At each "Learn" review, read them and compare them with `template/` and `README.md`.

Rules for the review:

- Write the findings to `kb/research/sources-YYYY-MM-DD.md`. The file starts with "Status: research, not approved".
- The owner runs `/doctor prompt-audit template` (only the owner can type it). Add its findings to the same research file.
- Propose three changes at most. Each one names the source, the rule it changes, and why.
- Do not edit `template/` or `README.md` in the review. A change needs the owner's yes first.
- After the review, set the "Last read" date below.
- Only the owner adds a page to this list.

Last read: 2026-11-13 (see `kb/research/sources-2026-11-13.md` for which pages were read in full)

## Claude Code

- [Changelog](https://code.claude.com/docs/en/changelog): new and changed features.
- [Best practices](https://code.claude.com/docs/en/best-practices)
- [Memory](https://code.claude.com/docs/en/memory): `CLAUDE.md` and imports.
- [Settings](https://code.claude.com/docs/en/settings)
- [Permissions](https://code.claude.com/docs/en/permissions): the rule formats in `template/.claude/settings.json`.
- [Subagents](https://code.claude.com/docs/en/sub-agents): the format of `template/.claude/agents/reviewer.md`.
- [Skills](https://code.claude.com/docs/en/skills)
- [Hooks](https://code.claude.com/docs/en/hooks)

## Prompting and agents

- [Anthropic, "Prompting best practices"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic, "Prompting Claude Fable 5.2"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- [Anthropic engineering blog](https://www.anthropic.com/engineering)
- [Anthropic, "Building agents: When to fold subagents into your main agent loop"](https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
- [Cognition, "Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working)
