"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, for local runs) and prints it.

The line: a dev excuse whose twist lands on the last words — the tests
passed only because the dev mocked the database, the network, and,
in hindsight, reality itself. Correct jargon, one line, every word
earns its place, and a fresh turn on the well-worn "tests passed"
excuse rather than a retread of "it worked on my machine".
"""

import os

ENTRY = (
    "The tests all passed \u2014 I'd mocked the database, "
    "the network, and, in hindsight, reality itself."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} chars, 1 line)")


if __name__ == "__main__":
    main()
