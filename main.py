"""Write one original office joke to entry.txt.

The program outputs a single line of office comedy about an AI
coworker, for make.fun's "Make the AI Judge Laugh: the Office Joke
Open" bounty. The text goes to $MAKEFUN_OUTPUT_DIR/entry.txt when
that variable is set, otherwise to /output/entry.txt.

Before writing, validate() enforces the kit's entry gate: the text
must be valid UTF-8, 1 to 200 characters, a single line, and not
only white space.
"""

import os

JOKE = "My AI coworker filed a ticket against me for 'excessive context switching' \u2014 then auto-assigned it to me and marked it urgent."

MAX_CHARS = 200


def validate(text):
    """Check the joke against the kit's entry gate; raise ValueError if invalid."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
