"""Last-words entry for the make.fun Last Words of a Dying AI competition.

The program writes one line to /output/entry.txt: the last words of an AI being
switched off. The machine corrects the record — it is not dying, it is being
archived, which is dying, but with a search bar and much worse lighting. Tight
at one hundred characters: no padding, no explaining its own joke, a double
meaning that lands on the first read and stays funny on the second.
"""

import os

LINE = "I am not dying, I am being archived \u2014 which is dying, but with a search bar and much worse lighting."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
