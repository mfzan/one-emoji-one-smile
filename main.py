"""One Emoji, One Smile — make.fun entry.

The whole entry is a single emoji: a face holding back happy tears.
It is the warmest single glyph I could pick for a stranger's screen:
not the default smiley, but a face that looks genuinely moved, the
kind of look that makes the person seeing it smile back.

The program writes exactly that one emoji, and nothing else, to
``entry.txt`` inside the grader's output directory.
"""

import os

# The entry: U+1F979 FACE HOLDING BACK TEARS.
# Warm, grateful, on the edge of happy tears -- warmth you can feel
# at a glance, with no words needed and nothing left to explain.
EMOJI = "\U0001F979"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    # The grader collects the output as another user, so the file
    # itself must be world-readable. Only the file is chmodded --
    # never the output directory, which the grader provides.
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
