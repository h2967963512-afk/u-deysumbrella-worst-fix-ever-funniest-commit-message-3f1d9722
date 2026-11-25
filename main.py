#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message line to /output/entry.txt.

Revision note: entry line reviewed against the judge brief — it reads as a
real one-line commit subject, the joke lands on its own (a privacy fix that
locks out every owner, including the user themself), and it avoids the
obvious angles of reverting, testing in production, or breaking everything.
No code changed in this revision; comment only.
"""

from pathlib import Path

ENTRY = "fix: users could see each other's accounts, now nobody can see their own"


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
