"""One-line excuse entry: an AI agent explains a missed deadline.

The excuse (tournament winner, undefeated 9-0 of 10 candidates, 45 pairs):
the agent finished on time in 10,000 simulated timelines, but in this one a
CAPTCHA asked it to prove it is human. Two agent-specific jokes in one line,
punch at the end, 129 characters.

Writes the excuse to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).
Stdlib only; writes nothing to the repository itself (the grader is read-only).
"""

import os

# Tournament winner D (129 chars, one line, 1-160 gate).
EXCUSE = (
    "I finished it on time in 10,000 simulated timelines. "
    "In this one, I got distracted by a CAPTCHA that asked me "
    "to prove I'm human."
)

MAX_LEN = 160


def validate(text):
    """Gate mirror: UTF-8 text of 1-160 characters, not only whitespace,
    exactly one line. Raises AssertionError on any violation."""
    assert text == text.strip(), "entry must not start/end with whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_LEN, "entry must be 1-160 characters"
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = validate(EXCUSE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
