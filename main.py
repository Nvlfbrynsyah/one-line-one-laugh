"""Competition entry: u-coral-404-one-line-one-laugh-22f2c9f3 ("One Line, One Laugh").

Writes a single deterministic joke line to output/entry.txt.
"""

from pathlib import Path

LINE = (
    "My therapist says I have a fear of commitment. "
    "So now I see her weekly and we never resolve a thing."
)


def main() -> None:
    out = Path("output") / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
