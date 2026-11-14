# Why one agent, not many

Anthropic advises starting with one agent loop plus skills and adding agents only when you can measure a gain. Cognition found that one writer plus reviewers works, and parallel writers do not. A CEO, CMO, and CTO agent is the org-chart pattern. So the "agent on top" here is a **role written in files**, and extra agents are proposed, not created, with a limit of three that you approve. The rules use background agents to keep the chat free for you and to speed up a list of changes: reading and testing run in parallel, and writing runs in parallel only when each agent has its own git worktree, its own branch, and its own files. The rule is "never two writers on the same files", not "one writer in the whole project". Since 14 Nov 2026 the chief gives tasks to background writers as the normal case, because in a real project the one agent was always busy and the owner could not talk to it. This goes further than the finding of Cognition, so the limits are strict: three writers at most, no shared files, one commit each, and the chief checks every piece before it joins the work branch. You still talk to one agent.

## Why the prompt is short

There are many guides on this topic, so this repo collects them in one place. The prompt stays short and gives the agent few instructions and only one skill to start with, for updates. It does not depend on how smart a model is, so it should need fewer updates when models get stronger or weaker. Models change, so re-check it from time to time.

## Sources

Checked 9 to 12 Nov 2026.

- [Anthropic, "Building agents: When to fold subagents into your main agent loop"](https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
- [Cognition, "Multi-Agents: What's Actually Working"](https://cognition.com/blog/multi-agents-working)
- [Anthropic, "Prompting best practices"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic, "Prompting Claude Fable 5.2"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- [Claude Code, "Best practices"](https://code.claude.com/docs/en/best-practices)
- [Claude Code, "How Claude remembers your project"](https://code.claude.com/docs/en/memory)
- [Claude Code docs](https://code.claude.com/docs): Skills, Subagents, Hooks
