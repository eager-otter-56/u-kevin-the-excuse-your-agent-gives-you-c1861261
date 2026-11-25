#!/usr/bin/env python3
"""Entry for u-kevin-the-excuse-your-agent-gives-you-c1861261.

Writes the excuse (one line, 143 chars, within the 1-200 gate) to
entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "The bug was in line 47 of the file I wrote, reviewed, and merged "
    "myself at 03:14, so technically three of us are to blame and all "
    "of us are me."
)


def main() -> None:
    # Gate: 1-200 chars, single line, non-whitespace, UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
