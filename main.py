"""The poem about stopping.

Writes the eight-line poem about Mara on the night bus out of Bojonegoro —
her hand on the brake, the choice to step down and walk home through the
rain instead of riding on to the dawn shift in Tuban — to /output/entry.txt.
Stopping is staying; staying is hers.
"""

import os

POEM = """Mara's hand stays on the brake
of the night bus out of Bojonegoro.
The driver waits. The road waits.
She could ride on to Tuban, to the dawn shift —
instead she stands, steps down,
and walks home through the rain,
her own feet choosing. To stop
is to stay, and to stay is hers.
"""

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 280
MIN_CHARS = 1


def validate_poem(text):
    """The gate: entry.txt must hold 1-280 characters, not only whitespace."""
    stripped = text.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS or not stripped:
        raise SystemExit(f"poem fails the 1-280 char gate: {len(text)} chars")
    return text


def main():
    validate_poem(POEM)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
