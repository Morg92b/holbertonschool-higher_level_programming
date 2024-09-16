#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """
    Class representing a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given private size and position.
        Validates that size is an integer and >= 0.
        Validates that position is a tuple of 2 positive integers.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.
        Validates that the new value is a tuple of 2 positive integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size ** 2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.
        Prints an empty line if size is 0.
        Considers the position to determine spacing.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
