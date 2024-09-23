#!/usr/bin/python3
"""
That a class file for rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     A subclass of BaseGeometry that represents a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes width and height after validating them
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
