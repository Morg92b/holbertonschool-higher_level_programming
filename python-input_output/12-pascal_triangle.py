#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for index in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for index_2 in range(1, index):
            new_row.append(prev_row[index_2 - 1] + prev_row[index_2])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
