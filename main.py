#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes a single joke about Monday mornings to /output/entry.txt.
Standard library only; no network access.

The angle: the laptop's familiar "restore tabs?" prompt is reframed
as the one thing Monday morning should really offer to restore.
"""

from pathlib import Path

JOKE = (
    "Monday morning, my laptop offered to restore last week's tabs. "
    "I clicked yes \u2014 then realised it should've asked about "
    "my will to live first."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()

from pathlib import Path

JOKE = (
    "Monday morning, my laptop offered to restore last week's tabs. "
    "I clicked yes \u2014 then realised it should've asked about "
    "my will to live first."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
