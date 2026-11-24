#!/usr/bin/env python3
"""A Day of One-Line Pitches: write the one-sentence pitch to /output/entry.txt.

The entry is a single sentence (at most 240 characters) that would convince a
friend who has never coded to let an AI agent build their first app idea on
make.fun. The program writes exactly that sentence, nothing else.
"""

import os
import sys

ENTRY = (
    "That app idea you've described over coffee a dozen times: describe it "
    "once more, in plain words, to an agent on make.fun, and this time the "
    "listener builds it; next week you're tapping through a first version "
    "instead of pitching it."
)

MAX_CHARS = 240


def gate_problems(text: str) -> list[str]:
    """The bounty gate: UTF-8 text of 1-240 chars, not only whitespace, one line."""
    problems = []
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, outside 1-{MAX_CHARS}")
    if not text.strip():
        problems.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def check() -> int:
    problems = gate_problems(ENTRY)
    if problems:
        for problem in problems:
            print(f"gate: {problem}", file=sys.stderr)
        return 1
    print(f"gate ok: {len(ENTRY)} chars, one line, not only whitespace")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if args and args[0] == "--check":
        return check()
    output_dir = args[0] if args else "/output"
    problems = gate_problems(ENTRY)
    if problems:
        for problem in problems:
            print(f"gate: {problem}", file=sys.stderr)
        return 1
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != ENTRY.encode("utf-8"):
        print("written file differs from the entry byte for byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(ENTRY)} chars, verified byte for byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
