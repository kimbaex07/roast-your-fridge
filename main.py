"""Roast Your Fridge entry generator.

Writes a single-line roast of the author's fridge to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Pure Python 3 standard library only. Deterministic: no randomness,
no network, no time dependence. The entry text is a fixed constant
below; this program only self-checks it against the competition gate
before writing it out.
"""

import os
import stat
import sys

ENTRY = (
    "My fridge has a light that turns on every time I open it, "
    "like it's proud of the three condiments and one sad carrot inside."
)


def self_check(text):
    """Enforce the competition gate before writing anything."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )


def main():
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
