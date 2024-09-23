#!/usr/bin/python3
"""
That a class file for square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle that represents a square
    """
    def __init__(self, size):
        """
        Initializes size after validating it
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a formatted string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
