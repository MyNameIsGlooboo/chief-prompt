"""Check the template files and the prompt. No model, no network, standard library only.

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
PROMPT_MAX_WORDS = 400

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
REQUIRED_GITIGNORE = [".env", ".env.*", ".secrets/", ".obsidian/"]
REQUIRED_IMPORTS = ["@kb/status.md", "@kb/todo.md"]
REVIEWER_TOOLS = "tools: Read, Grep, Glob"
# This repo uses its own prompt. These root files must be exact copies of the template.
ROOT_COPIES = [RULES_FILE, ".claude/settings.json", ".claude/agents/reviewer.md", ".gitignore"]
# Files the prompt must name, so the agent copies all of them.
PROMPT_MUST_NAME = [RULES_FILE, "CLAUDE.md", ".gitignore", ".claude/settings.json", ".claude/agents/reviewer.md"]
# The prompt must tell the agent to keep files that already exist.
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
    check("allow" not in permissions, "settings.json has no allow rules")


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


def check_rules():
    text = read(TEMPLATE / RULES_FILE)
    if text is None:
        return
    lines = text.splitlines()
    check(len(lines) < RULES_MAX_LINES, f"the rules file is under {RULES_MAX_LINES} lines ({len(lines)})")
    check("one main agent, no team" in text, "the rules file has the chief-of-staff line")
    # An import in this file would resolve from .claude/rules/, not from the project root.
    imports = [line for line in lines if re.search(r"(^|\s)@[\w./~-]+", line)]
    check(not imports, "the rules file has no import")
    check("Talk to me in" not in text, "the rules file has no Language line (it lives in CLAUDE.md)")


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
    text = read(ROOT / "README.md")
    if text is None:
        return
    blocks = re.findall(r"```text\n(.*?)```", text, re.DOTALL)
    check(len(blocks) == 1, "README.md has exactly one prompt block")
    if len(blocks) != 1:
        return
    prompt = blocks[0]
    words = len(prompt.split())
    check(words <= PROMPT_MAX_WORDS, f"prompt is at most {PROMPT_MAX_WORDS} words ({words})")
    for name in PROMPT_MUST_NAME:
        check(name in prompt, f"prompt names {name}")
    check("/template" in prompt or "template/" in prompt, "prompt points to the template folder")
    for phrase in PROMPT_MUST_SAY:
        check(phrase in prompt, f"prompt says '{phrase}'")


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


check_settings()
check_root_copies()
check_reviewer()
check_rules()
check_claude_md()
check_gitignore()
check_prompt()

print()
if failures:
    print(f"{len(failures)} check(s) failed.")
    sys.exit(1)
print("All checks passed.")
