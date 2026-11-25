"""Monday Morning Punchlines — entry writer (v2 final).

Writes the entry joke to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to /output, then ./output.
Pure standard library; deterministic output.

Entry chosen by a 24-candidate, 8-seed knockout tournament scored
against the judge brief's five criteria in order (see candidates.md):
the bed-custody line won the final over the negotiation line.
"""

import os
import sys

# v2 final line (tournament winner): the bed files for custody.
ENTRY = (
    "My bed filed for custody of me on Monday mornings. "
    "The judge ruled in its favour."
)

MAX_CHARS = 200


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
