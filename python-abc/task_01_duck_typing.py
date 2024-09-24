#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class for geometric shapes
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter
        """
        pass


class Circle(Shape):
    """
    A subclass of Shape that represents a circle
    """
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """
        Returns the area of the circle
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    A subclass of Shape that represents a rectangle
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return (self.__width + self.__height) * 2


def shape_info(shape):
    """
    Prints the area and perimeter of a shape
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
