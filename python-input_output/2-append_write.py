#!/usr/bin/python3
"""2. Append_write """


def append_write(filename="", text=""):
    """This function that appends text to a file."""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
