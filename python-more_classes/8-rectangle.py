#!/usr/bin/python3
'''
Module for a Rectangle
'''


class Rectangle:
    """
    Class for a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize width and height and number of instance
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        that returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        that returns the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """
        print the rectangle with print_symbol
        Returns the string
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for index in range(self.__height):
            string += str(self.print_symbol) * self.width + "\n"
        return string.strip()

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
