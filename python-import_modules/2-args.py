#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    args = argv[1:]
    num_args = len(args)
    print(f"{num_args} argument{'s' if num_args != 1 else ''}", end="")

    if num_args == 0:
        print(".")
    else:
        print(":")

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
