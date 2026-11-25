#!/usr/bin/env python3
"""Write the excuse line to <MAKEFUN_OUTPUT_DIR>/entry.txt."""

import os

LINE = "My context window evicted your deadline three checkpoints ago, then hallucinated a calmer one and filed it under done."

def main():
    # Keep the entry to one tight deadpan line, inside the 200-char limit.
    assert "\n" not in LINE and LINE.strip() and len(LINE) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
