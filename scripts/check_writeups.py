#!/usr/bin/env python3
"""Sanity checks for the writeups in this repository.

Run from the repository root:

    python scripts/check_writeups.py

Checks (exit code 1 if any fails):
  1. No unredacted CTF flags (THM{...}, HTB{...}, flag{...}) in any Markdown file.
  2. Every writeup under tryhackme/ has Platform and Status metadata lines.
  3. Every writeup under tryhackme/ is linked from the root README index.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WRITEUP_ROOT = ROOT / "tryhackme"

FLAG_RE = re.compile(r"\b(?:THM|HTB|BTLO|flag|CTF)\{([^}]*)\}", re.IGNORECASE)
ALLOWED_FLAG_BODIES = {"REDACTED", "...", "redacted"}


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_flags(files: list[Path]) -> list[str]:
    problems = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in FLAG_RE.finditer(text):
            if match.group(1) not in ALLOWED_FLAG_BODIES:
                line = text.count("\n", 0, match.start()) + 1
                problems.append(f"{path.relative_to(ROOT)}:{line}: unredacted flag-like string")
    return problems


def check_metadata(writeups: list[Path]) -> list[str]:
    problems = []
    for path in writeups:
        text = path.read_text(encoding="utf-8")
        for field in ("Platform", "Status"):
            if f"**{field}:**" not in text:
                problems.append(f"{path.relative_to(ROOT)}: missing '**{field}:**' line")
    return problems


def check_index(writeups: list[Path]) -> list[str]:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    problems = []
    for path in writeups:
        rel = path.relative_to(ROOT).as_posix()
        if rel not in readme:
            problems.append(f"{rel}: not linked from README.md index")
    return problems


def main() -> int:
    files = markdown_files()
    writeups = sorted(WRITEUP_ROOT.rglob("README.md"))
    problems = check_flags(files) + check_metadata(writeups) + check_index(writeups)
    for problem in problems:
        print(problem)
    print(f"Checked {len(files)} Markdown files, {len(writeups)} writeups: "
          f"{len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
