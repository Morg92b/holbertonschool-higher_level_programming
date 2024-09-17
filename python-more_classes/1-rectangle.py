#!/usr/bin/python3
'''
Module for a Rectangle
'''


class Rectangle:
    """
    Class for a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize width and height.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Get the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width, with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height, with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
