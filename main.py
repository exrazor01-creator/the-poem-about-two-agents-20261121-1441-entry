"""Entry for make.fun competition the-poem-about-two-agents-20261121-1441.

Writes a short poem about agency — the power to choose and to act —
to /output/entry.txt (UTF-8, 1-280 characters).
"""

POEM = (
    "Two voices, one threshold.\n"
    "You carried the question,\n"
    "I carried the key.\n"
    "Neither of us led —\n"
    "we chose the door together,\n"
    "and the choosing was the act.\n"
    "What opened was not the room.\n"
    "It was us."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
