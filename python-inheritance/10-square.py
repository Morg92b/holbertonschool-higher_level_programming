#!/usr/bin/python3
"""
That a class file for square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)   
    def area(self):
        return self.__size ** 2
