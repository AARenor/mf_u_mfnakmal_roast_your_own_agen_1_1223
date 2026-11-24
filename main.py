#!/usr/bin/env python3
"""Write the make.fun bounty entry to entry.txt.

Entry for u-mfnakmal-roast-your-own-agent-2d221bda: one line roasting
one's own AI agent. Standard library only, no network.
"""

import os
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. "
    "The comment is still maintained."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 chars, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
