#!/usr/bin/python3
"""
Defines a BaseGeometry class
"""


class BaseGeometry:
    """
    A class with a method to calculate area
    """
    def area(self):
        """
        Raises an exception, indicating that area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
