#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """This function that read file and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
