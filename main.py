#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first word that comes to mind, to
/output/entry.txt, then reads it back and verifies it matches exactly.
"""

import os
import sys

WORD = "tsundoku"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="ascii") as f:
        f.write(WORD + "\n")

    with open(OUTPUT_PATH, "r", encoding="ascii") as f:
        content = f.read()

    # Exactly one word, one line, ASCII letters only, nothing else.
    lines = content.splitlines()
    if content != WORD + "\n" or len(lines) != 1 or not lines[0].isalpha():
        print(f"verification failed: entry.txt holds {content!r}", file=sys.stderr)
        return 1

    print(f"entry written and verified: {WORD!r} -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
