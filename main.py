"""Two Lines to Your Past Self.

Writes exactly two lines to entry.txt:
  line 1 - a warning to my past self about one specific moment;
  line 2 - why that moment mattered and what changed because of it.
Standard library only.
"""

import os

LINE_1 = "Don't skip your father's call on the night of 14 March \u2014 pick up, even though you're angry."
LINE_2 = "It was the last time he ever called, and answering is why you pick up every call since, no matter how angry you are."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
