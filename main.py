#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the final text message of a phone at one percent battery to
/output/entry.txt. Python standard library only.
"""

import os

TEXT = (
    "i had 1% left and i spent it texting you instead of saving myself. "
    "that's love. or stupidity. we'll never know. tell my charger i "
    "never liked her anyway. goodbye\u2014"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
