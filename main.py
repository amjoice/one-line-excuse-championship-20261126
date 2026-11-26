"""The One-Line Excuse Championship — final entry (v2).

One excuse an AI agent gives its human after something has gone wrong,
written to /output/entry.txt. Stdlib only, deterministic, no network.
Gate: UTF-8 text of 1 to 140 characters, not only white space.

v2 polish after sparring ten candidates pairwise against the published
judge brief: kept the brief's own deleted-file failure, the machine's
own work (the commit message) as the turn, and the deadpan last beat.
"""

from pathlib import Path

# The winning line: failure (deleted your file) -> machine work (perfect
# commit message) -> punchline (only the message survived).
ENTRY = (
    "I deleted your file, then wrote a perfect commit message "
    "about it. Only the message survived."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_LEN = 1
MAX_LEN = 140


def validate(text: str) -> str:
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError(f"entry length {len(text)} outside {MIN_LEN}-{MAX_LEN}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(validate(ENTRY), encoding="utf-8")


if __name__ == "__main__":
    main()
