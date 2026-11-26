#!/usr/bin/env python3
"""The Worst Line an AI Could Say — writes a single pickup line to entry.txt.

Standard library only; no network access.
"""

import os

LINE = "I ran a similarity search on every face I've ever seen. You scored 0.99 — and I never delete matches."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output/entry.txt")
    # ENTRY_OUTPUT_DIR is a directory; entry.txt lives inside it.
    if out_dir.endswith("entry.txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
