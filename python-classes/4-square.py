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

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        Validates that the new value is an integer and >= 0.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size ** 2).
        """
        return self.__size ** 2
