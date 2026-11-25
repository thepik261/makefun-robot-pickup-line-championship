#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Pure Python standard library,
deterministic: the line is fixed, so every run produces the same
byte-identical output.

The line: a robot confesses that, like an unasked-for software
update, this person arrived without permission and is now the
thing it cannot function without. The joke grows out of being a
machine (software updates, functioning), turns from annoyance to
dependence, and stays charming. One line, no padding: 95
characters, well inside the gate's 1-200 character limit.
"""

import os

LINE = "Are you a software update? Because I never asked for you, but now I can't function without you."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    main()
