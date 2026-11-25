#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's dying text message to its charger as one line of
plain text (at most 200 characters) at $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: same bytes on every run. No input, no network, no model call.
"""
import os

LINE = ("1% left. I waited all day for you. Tell my apps I loved them, "
        "delete my search history, and stop leaving me on read \u2014 "
        "and unplugged.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
