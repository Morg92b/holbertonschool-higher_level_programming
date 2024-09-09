#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row)
        for index in range(length):
            if index < length - 1:
                print("{:d}".format(row[index]), end=" ")
            else:
                print("{:d}".format(row[index]), end="")
        print()
