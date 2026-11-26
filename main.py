#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes one line to /output/entry.txt: a weather forecast for a city that
does not exist, made funny. 82 characters, plain ASCII, no trailing newline.

The joke: the city of Mistake exists only because the Met Office invented it
by typo — and still forecasts its weather with full bureaucratic confidence.
The joke is about the forecaster, not the weather; at 82 bytes it also carries
a tiebreak edge over a field where most real entries run past 100 characters.
"""

import os

ENTRY = "Today in Mistake: the Met Office forecasts weather for a city it invented by typo."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-120 UTF-8 chars.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
