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


def main() -> int:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(f"entry is {len(ENTRY)} chars, outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
