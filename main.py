"""Unsent: The Micro-Confession Sprint entry.

Writes a two-part micro-confession (a To: line and the one unsent
line itself) to /output/entry.txt. The competition gate requires
UTF-8 text of 1 to 260 characters in total, not only white space,
with the unsent message itself a single line of at most 200
characters. The program is deterministic: every run writes exactly
the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_TOTAL_CHARS = 260
MAX_MESSAGE_CHARS = 200

TO_LINE = "To: my little brother"
MESSAGE = (
    "i still play dad's last voicemail to hear him call you by the name only he used. "
    "i miss him more than i miss you, and you've been gone longer."
)


def build_entry() -> str:
    return TO_LINE + "\n" + MESSAGE


def main() -> None:
    text = build_entry()
    assert 1 <= len(text) <= MAX_TOTAL_CHARS, (
        f"entry must be 1..{MAX_TOTAL_CHARS} characters, got {len(text)}"
    )
    assert len(MESSAGE) <= MAX_MESSAGE_CHARS, (
        f"message must be at most {MAX_MESSAGE_CHARS} characters, got {len(MESSAGE)}"
    )
    assert "\n" not in MESSAGE, "the unsent message must be a single line"
    assert text.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
