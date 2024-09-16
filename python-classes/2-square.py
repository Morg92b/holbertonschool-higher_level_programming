#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    Class representing a square
    """
    def __init__(self, size=0):
        """
        Initialize a square with a given private size.
        Validates that size is an integer and >= 0.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
