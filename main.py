#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes one original one-liner to /output/entry.txt, in the voice of a
cron job handing in its notice.

The joke: a cron job that has fired every minute since March, invisible
labour nobody ever acknowledged. The one human who finally noticed it
was the on-call engineer at 3 a.m. -- and his only response was to mute
it. The punch lands on the last words: even being noticed was just
another way of being ignored.

The line is fixed text, written exactly as it appears below: one line,
no trailing newline, 133 characters, plain UTF-8.
"""

import os

# The resignation, the record of service, and the punch: the single
# human who ever noticed the job, and what he did about it. Joined with
# an em dash, the pivot the joke turns on.
OPENING = "I resign: I have fired every minute since March"
MIDDLE = "and the only human who ever noticed me was on call at 3 a.m."
PUNCH = "and he just muted me."

LINE = OPENING + ", " + MIDDLE + " \u2014 " + PUNCH


def validate_line(text):
    """One fixed line: 1-140 characters, no newline, no trailing space."""
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have surrounding whitespace"


def main() -> None:
    text = LINE.strip()
    validate_line(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
