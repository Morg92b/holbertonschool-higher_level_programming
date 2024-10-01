#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """
    A class that defines a student by first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance.
        """
        return self.__dict__
