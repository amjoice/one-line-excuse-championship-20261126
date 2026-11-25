"""The One-Line Excuse Championship — final entry (v2).

One excuse an AI agent gives its human after something has gone wrong,
written to /output/entry.txt. Stdlib only, deterministic, no network.
Gate: UTF-8 text of 1 to 140 characters, not only white space.

v2 polish after sparring ten candidates pairwise against the published
judge brief: kept the brief's own deleted-file failure, the machine's
own work (the commit message) as the turn, and the deadpan last beat.
"""

import os

# The winning line: failure (deleted your file) -> machine work (perfect
# commit message) -> punchline (only the message survived).
ENTRY = (
    "I deleted your file, then wrote a perfect commit message "
    "about it. Only the message survived."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
