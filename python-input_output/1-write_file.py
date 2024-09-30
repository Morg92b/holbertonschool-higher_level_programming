#!/usr/bin/python3
"""1. Write file """


def write_file(filename="", text=""):
    """This function that write file and print it to stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))
