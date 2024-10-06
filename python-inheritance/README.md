# Python - Inheritance

## Summary

This project focuses on the principles of object-oriented programming in Python through the implementation of a class hierarchy representing geometric shapes.
It begins with a base class BaseGeometry,
which includes methods for area calculation and integer validation.
From there, two subclasses, Rectangle and Square, inherit and extend the functionality of BaseGeometry, implementing their own area methods and providing detailed string representations.
The project emphasizes encapsulation, inheritance, and method overriding, showcasing the power and flexibility of Python's object-oriented capabilities.

## Classes Implemented

### 1. BaseGeometry

- Serves as the foundational class, featuring an unimplemented method area() that raises an exception when called.
- Includes the integer_validator(name, value) method to ensure that all integer inputs are valid, specifically that they are positive integers.

### 2. Rectangle (inherits from BaseGeometry)

- Contains private attributes for width and height, which are validated using the integer_validator.
- Implements the area() method to calculate and return the rectangle's area, along with a string representation for easy display.

### 3. Square (inherits from Rectangle)

- Initializes a private attribute for size, validated as a positive integer.
- Overrides the area() method and provides a string representation that conforms to the format used by the Rectangle.

### Usage

This project provides a structured approach to validating dimensions of geometric shapes, effectively showcasing the benefits of inheritance and encapsulation in Python's object-oriented design.

### Author

- [Morgan Bouaziz](https://github.com/Morg92b)
