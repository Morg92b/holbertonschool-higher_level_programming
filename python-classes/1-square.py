#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    Class representing a square
    """
    def __init__(self, size):
        """
        Initialize a square with a given private size
        Args:
            size (int): The size of the square
        """
        self.__size = size
