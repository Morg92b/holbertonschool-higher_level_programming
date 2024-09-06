#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n = len(argv)
    op_add = 0
    for i in range(1, n):
        op_add += int(argv[i])
    print(f"{op_add}")
