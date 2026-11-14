"""Check the template files, the setup steps and the line to paste. No model, no network, standard library only.

Run from the repo root:  python scripts/check.py
Exit code 0 means every check passed.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template"

CLAUDE_MD_MAX_LINES = 100
RULES_MAX_LINES = 100
RULES_FILE = ".claude/rules/chief-of-staff.md"
UPDATE_SKILL = ".claude/skills/chief-update/SKILL.md"
AUTOPILOT_SKILL = ".claude/skills/chief-autopilot/SKILL.md"
# Autopilot runs with nobody there. Its skill must name each action it never does.
AUTOPILOT_NEVER = ["git push", "git merge", "gh pr merge", "gh repo create", "deleting a file", "kb/approved/plan.md", "publishing", "deploying", "paying"]
PROMPT_MAX_WORDS = 400
README_MAX_LINES = 165
README_DIAGRAMS = 5
# The long parts of the README live here. README.md must link to each one.
DOCS = ["docs/guide.md", "docs/limits.md", "docs/why-one-agent.md", "docs/maintainer.md"]
SETUP_FILE = "template/SETUP.md"
SOURCE_REPO = "https://github.com/MyNameIsGlooboo/chief-prompt"

REQUIRED_DENY = ["Read(.env)", "Read(.env.*)", "Read(/.secrets/**)"]
REQUIRED_ASK = [
    "Bash(git push *)",
    "Bash(git merge *)",
    "Bash(gh pr merge *)",
    "Bash(gh repo create *)",
    "Bash(rm *)",
    "PowerShell(git push *)",
    "PowerShell(git merge *)",
    "PowerShell(gh pr merge *)",
    "PowerShell(gh repo create *)",
    "PowerShell(Remove-Item *)",
    "Edit(/kb/approved/plan.md)",
]
# The only allow rules: the two browsers, WebFetch and WebSearch. Any other allow rule fails the check.
REQUIRED_ALLOW = ["mcp__claude-in-chrome__*", "mcp__Claude_Browser__*", "WebFetch", "WebSearch"]
# .claude/worktrees/ holds the worktrees of background writers. Without the line, git status shows them.
REQUIRED_GITIGNORE = [".env", ".env.*", ".secrets/", ".obsidian/", ".claude/worktrees/"]
REQUIRED_IMPORTS = ["@kb/status.md", "@kb/todo.md"]
REVIEWER_TOOLS = "tools: Read, Grep, Glob"
WRITER_FILE = ".claude/agents/writer.md"
# The writer has no Agent tool and no MCP tools: an exact list, so it cannot start agents or use a browser.
WRITER_TOOLS = "tools: Read, Grep, Glob, Edit, Write, Bash, PowerShell"
# The writer must work in its own worktree, stay in the background, and start without CLAUDE.md and the rules file.
WRITER_LINES = ["name: writer", "isolation: worktree", "background: true", "omitClaudeMd: true"]
# The words in the rules file that say who the chief is.
CHIEF_LINE = "the one agent I talk to"
# This repo uses its own prompt. These root files must be exact copies of the template.
ROOT_COPIES = [RULES_FILE, UPDATE_SKILL, AUTOPILOT_SKILL, ".claude/settings.json", ".claude/agents/reviewer.md", WRITER_FILE, ".gitignore"]
# Files the setup steps must name, so the agent copies all of them.
PROMPT_MUST_NAME = [RULES_FILE, UPDATE_SKILL, AUTOPILOT_SKILL, "CLAUDE.md", ".gitignore", ".claude/settings.json", ".claude/agents/reviewer.md", WRITER_FILE]
# The setup steps must tell the agent to keep files that already exist.
PROMPT_MUST_SAY = ["never replace", "Add only what is missing"]

failures = []


def check(ok, message):
    print(("PASS  " if ok else "FAIL  ") + message)
    if not ok:
        failures.append(message)


def read(path):
    if not path.is_file():
        check(False, f"{path.relative_to(ROOT).as_posix()} exists")
        return None
    return path.read_text(encoding="utf-8")


def check_settings():
    text = read(TEMPLATE / ".claude" / "settings.json")
    if text is None:
        return
    try:
        permissions = json.loads(text).get("permissions", {})
    except json.JSONDecodeError as error:
        check(False, f"settings.json is valid JSON ({error})")
        return
    check(True, "settings.json is valid JSON")
    deny = permissions.get("deny", [])
    ask = permissions.get("ask", [])
    for rule in REQUIRED_DENY:
        check(rule in deny, f"settings.json denies {rule}")
    for rule in REQUIRED_ASK:
        check(rule in ask, f"settings.json asks before {rule}")
    allow = permissions.get("allow", [])
    for rule in REQUIRED_ALLOW:
        check(rule in allow, f"settings.json allows {rule}")
    check(set(allow) <= set(REQUIRED_ALLOW), "settings.json has no other allow rules")


def check_reviewer():
    text = read(TEMPLATE / ".claude" / "agents" / "reviewer.md")
    if text is None:
        return
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    check(match is not None, "reviewer.md starts with frontmatter")
    if match is None:
        return
    lines = match.group(1).splitlines()
    tools = [line for line in lines if line.startswith("tools:")]
    check(tools == [REVIEWER_TOOLS], f"reviewer.md has exactly '{REVIEWER_TOOLS}'")
    check("name: reviewer" in lines, "reviewer.md is named reviewer")


def check_writer():
    text = read(TEMPLATE / WRITER_FILE)
    if text is None:
        return
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    check(match is not None, "writer.md starts with frontmatter")
    if match is None:
        return
    lines = match.group(1).splitlines()
    tools = [line for line in lines if line.startswith("tools:")]
    check(tools == [WRITER_TOOLS], f"writer.md has exactly '{WRITER_TOOLS}'")
    for line in WRITER_LINES:
        check(line in lines, f"writer.md has '{line}'")
    check(any(line.startswith("model: ") for line in lines), "writer.md names a model")
    check(any(line.startswith("description: ") for line in lines), "writer.md has a description")
    body = text[match.end():]
    # A writer that touches kb/ or pushes breaks the chief's rules for parallel work.
    for phrase in ["Do not touch `kb/`", "push", "One commit", "git add -A"]:
        check(phrase.lower() in body.lower(), f"writer.md names: {phrase}")


def check_rules():
    text = read(TEMPLATE / RULES_FILE)
    if text is None:
        return
    lines = text.splitlines()
    check(len(lines) < RULES_MAX_LINES, f"the rules file is under {RULES_MAX_LINES} lines ({len(lines)})")
    check(CHIEF_LINE in text, "the rules file has the chief-of-staff line")
    # The chief brings the work of its writers together with cherry-pick, because git merge has an ask rule.
    check("git cherry-pick" in text, "the rules file names git cherry-pick for the work of writers")
    # A writer works where the ask rule for the plan may not reach. The chief must look at the files of a commit before the pick.
    check("git show --stat" in text, "the rules file checks the files of a commit before a pick")
    # An import in this file would resolve from .claude/rules/, not from the project root.
    imports = [line for line in lines if re.search(r"(^|\s)@[\w./~-]+", line)]
    check(not imports, "the rules file has no import")
    check("Talk to me in" not in text, "the rules file has no Language line (it lives in CLAUDE.md)")


def check_update_skill():
    text = read(TEMPLATE / UPDATE_SKILL)
    if text is None:
        return
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    check(match is not None, "the update skill starts with frontmatter")
    if match is None:
        return
    lines = match.group(1).splitlines()
    check("name: chief-update" in lines, "the update skill is named chief-update")
    check(any(line.startswith("description: ") for line in lines), "the update skill has a description")
    # The skill changes files, so only the user may start it.
    check("disable-model-invocation: true" in lines, "only the user can start the update skill")
    body = text[match.end():]
    check("github.com/MyNameIsGlooboo/chief-prompt" in body, "the update skill names the source repo")
    # The three files the prompt owns. The skill must replace each one, or it never gets newer itself.
    for name in [RULES_FILE, UPDATE_SKILL, AUTOPILOT_SKILL]:
        check(name in body, f"the update skill replaces {name}")
    # The files that belong to the project. The skill must name each one.
    for name in ["CLAUDE.md", ".gitignore", ".claude/settings.json", ".claude/agents/reviewer.md", WRITER_FILE]:
        check(name in body, f"the update skill handles {name}")
    # The update line makes the agent read this file from a clone. The skill must not clone a second time.
    check("use that clone" in body, "the update skill uses the clone it was read from")


def check_autopilot_skill():
    text = read(TEMPLATE / AUTOPILOT_SKILL)
    if text is None:
        return
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    check(match is not None, "the autopilot skill starts with frontmatter")
    if match is None:
        return
    lines = match.group(1).splitlines()
    check("name: chief-autopilot" in lines, "the autopilot skill is named chief-autopilot")
    check(any(line.startswith("description: ") for line in lines), "the autopilot skill has a description")
    # The mode is the user's choice. The agent must never turn it on by itself.
    check("disable-model-invocation: true" in lines, "only the user can start the autopilot skill")
    body = text[match.end():]
    never = body.split("## Never in autopilot")[1].split("\n## ")[0] if "## Never in autopilot" in body else ""
    check(bool(never), "the autopilot skill has the part 'Never in autopilot'")
    for action in AUTOPILOT_NEVER:
        check(action in never, f"the autopilot skill never does: {action}")
    check("kb/research/autopilot-questions.md" in body, "the autopilot skill names the questions file")
    check("git show --stat" in body, "the autopilot skill checks the files of a commit before a pick")


def check_claude_md():
    text = read(TEMPLATE / "CLAUDE.md")
    if text is None:
        return
    lines = text.splitlines()
    check(len(lines) < CLAUDE_MD_MAX_LINES, f"CLAUDE.md is under {CLAUDE_MD_MAX_LINES} lines ({len(lines)})")
    last = [line for line in lines if line.strip()][-len(REQUIRED_IMPORTS):]
    check(last == REQUIRED_IMPORTS, "CLAUDE.md ends with @kb/status.md and @kb/todo.md")
    check("Talk to me in" in text, "CLAUDE.md has the Language line")


def check_gitignore():
    text = read(TEMPLATE / ".gitignore")
    if text is None:
        return
    entries = text.split()
    for entry in REQUIRED_GITIGNORE:
        check(entry in entries, f".gitignore has {entry}")


def check_prompt():
    # The one line in README.md that the user pastes.
    text = read(ROOT / "README.md")
    if text is not None:
        blocks = [block.strip() for block in re.findall(r"```text\n(.*?)```", text, re.DOTALL)]
        check(len(blocks) == 3, "README.md has exactly three blocks to paste: install, install with files, and update")
        # Two install lines: one for a new project, one for a project that already has files.
        install = [block for block in blocks if SETUP_FILE in block]
        check(len(install) == 2, f"two blocks to paste point to {SETUP_FILE}")
        for line in install:
            check("\n" not in line, "an install block is one line")
            check(SOURCE_REPO in line, "an install line names the source repo")
            check("My language:" in line, "an install line names a language")
        existing = [line for line in install if "already has files" in line]
        check(len(existing) == 1, "one install line is for a project that already has files")
        for line in existing:
            # The agent must not start while work is not committed, or git diff cannot show what it added.
            check("git status" in line, "the install line for a project with files checks git status first")
            check("Replace none of my own files" in line, "the install line for a project with files says to replace no file of the user")
            # In a folder with no git repo, git status fails and nothing can show or undo what the agent added.
            check("not a git repo" in line, "the install line for a project with files stops when there is no git repo")
        # The update line reads the update skill from the clone, so its steps are always the newest.
        update_file = "template/" + UPDATE_SKILL
        update = [block for block in blocks if update_file in block]
        check(len(update) == 1, f"one block to paste points to {update_file}")
        if len(update) == 1:
            line = update[0]
            check("\n" not in line, "the update block is one line")
            check(SOURCE_REPO in line, "the update line names the source repo")
            check(SETUP_FILE not in line, "the update line does not point to the setup steps")
    # The steps that the line points to.
    steps = read(ROOT / SETUP_FILE)
    if steps is None:
        return
    words = len(steps.split())
    check(words <= PROMPT_MAX_WORDS, f"{SETUP_FILE} is at most {PROMPT_MAX_WORDS} words ({words})")
    for number in range(1, 6):
        check(re.search(rf"^{number}\. ", steps, re.MULTILINE) is not None, f"{SETUP_FILE} has step {number}")
    for name in PROMPT_MUST_NAME:
        check(name in steps, f"{SETUP_FILE} names {name}")
    check("template/" in steps, f"{SETUP_FILE} points to the template folder")
    for phrase in PROMPT_MUST_SAY:
        check(phrase in steps, f"{SETUP_FILE} says '{phrase}'")


def check_root_copies():
    for name in ROOT_COPIES:
        source = read(TEMPLATE / name)
        copy = read(ROOT / name)
        if source is not None and copy is not None:
            check(source == copy, f"{name} in the repo root is the same as in template/")
    text = read(ROOT / "CLAUDE.md")
    if text is not None:
        lines = text.splitlines()
        check("Talk to me in" in text, "root CLAUDE.md has the Language line")
        # The rules now load from .claude/rules/. An import of the template would load a second copy.
        check("@template/" not in text, "root CLAUDE.md does not import from template/")
        last = [line for line in lines if line.strip()][-len(REQUIRED_IMPORTS):]
        check(last == REQUIRED_IMPORTS, "root CLAUDE.md ends with @kb/status.md and @kb/todo.md")
    for name in ["status.md", "todo.md"]:
        check((ROOT / "kb" / name).is_file(), f"kb/{name} exists")


def check_changelog():
    readme = read(ROOT / "README.md")
    changelog = read(ROOT / "CHANGELOG.md")
    if readme is None or changelog is None:
        return
    # The line must be near the top, so a reader sees how old the prompt is.
    top = "\n".join(readme.splitlines()[:5])
    match = re.search(r"^Last updated: (\d{4}-\d{2}-\d{2}), with Claude \S.*$", top, re.MULTILINE)
    check(match is not None, "README.md has the 'Last updated' line with a date and a model at the top")
    # Take every "## " heading, so an entry with a badly written date cannot be skipped.
    headings = re.findall(r"^## (.*)$", changelog, re.MULTILINE)
    dates = [heading for heading in headings if re.fullmatch(r"\d{4}-\d{2}-\d{2}", heading)]
    check(bool(dates), "CHANGELOG.md has at least one dated entry")
    check(dates == headings, "every '## ' heading in CHANGELOG.md is only a date (YYYY-MM-DD)")
    if match is None or not dates:
        return
    check(dates == sorted(dates, reverse=True), "CHANGELOG.md has the newest date first")
    check(match.group(1) == dates[0], f"the 'Last updated' date is the newest date in CHANGELOG.md ({dates[0]})")


def check_readme():
    text = read(ROOT / "README.md")
    if text is None:
        return
    lines = text.splitlines()
    check(len(lines) <= README_MAX_LINES, f"README.md is at most {README_MAX_LINES} lines ({len(lines)})")
    diagrams = len(re.findall(r"^```mermaid$", text, re.MULTILINE))
    check(diagrams == README_DIAGRAMS, f"README.md has {README_DIAGRAMS} diagrams ({diagrams})")
    for name in DOCS:
        if read(ROOT / name) is not None:
            check(f"]({name})" in text, f"README.md links to {name}")
    # A link in docs/ that starts at the repo root is broken on GitHub.
    for name in DOCS:
        doc = read(ROOT / name) or ""
        bad = re.findall(r"\]\((?:template|kb|scripts|\.claude|README\.md|CHANGELOG\.md|LICENSE)", doc)
        check(not bad, f"{name} has no link that starts at the repo root")


check_settings()
check_readme()
check_changelog()
check_root_copies()
check_reviewer()
check_writer()
check_rules()
check_update_skill()
check_autopilot_skill()
check_claude_md()
check_gitignore()
check_prompt()

print()
if failures:
    print(f"{len(failures)} check(s) failed.")
    sys.exit(1)
print("All checks passed.")
