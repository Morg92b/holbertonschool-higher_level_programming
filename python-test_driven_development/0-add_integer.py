#!/usr/bin/python3

"""
This function adds two numbers
"""


def add_integer(a, b=98):
    """
    Args:
        a: first number
        b: second number

    Return: The addition of two numbers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
