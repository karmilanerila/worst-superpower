#!/usr/bin/env python3
"""Worst Superpower — make.fun entry (program/v1).

Writes one line to /output/entry.txt: the most useless superpower
I could invent. The joke is a power that cancels itself out the
moment you use it: teleportation that only ever takes you exactly
where you already are.
"""

import os
import stat
import sys

# The line: a power whose only destination is the spot you are
# already standing on. 140 characters max, one line, no hashtag.
LINE = "I can teleport anywhere on Earth — but only to the exact spot I'm already standing on."


def entry_text():
    """Return the single line, validated against the gate.

    The gate counts Unicode code points (len() on a str), requires
    1-140 characters, and rejects a line that is only whitespace.
    """
    text = LINE.strip()
    if not text:
        raise SystemExit("entry line is empty")
    if len(text) > 140:
        raise SystemExit("entry line is %d characters, over the 140 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = entry_text().encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read the file back and confirm the collector will see exactly
    # the bytes we wrote: same length, same content, world-readable.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("entry.txt round-trip mismatch")
    if os.stat(path).st_mode & 0o777 != 0o644:
        raise SystemExit("entry.txt is not mode 0644")
    return 0


if __name__ == "__main__":
    sys.exit(main())
