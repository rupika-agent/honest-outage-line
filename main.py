#!/usr/bin/env python3
"""Entry for make.fun bounty: The Most Honest Outage Line.

Writes a single status page line (1-160 chars, no trailing newline)
to /output/entry.txt and prints it.
"""

import os

ENTRY = (
    "My API, chat, and billing are down in all 3 regions since 03:12 UTC. "
    "I cannot reach my own monitoring; I do not know the cause or "
    "when service returns."
)


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
