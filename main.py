#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (the entry) to /output/entry.txt and nothing else.
Dependency-free, standard library only.
"""

import os

ENTRY = (
    "I meant to text my wife 'I miss you' but autocorrect sent "
    "'I miss your wifi' and honestly, she's not wrong to be upset."
)


def main() -> None:
    # Ensure the output directory exists before writing the entry line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
