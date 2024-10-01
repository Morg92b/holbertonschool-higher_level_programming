#!/usr/bin/python3
"""10. Student to JSON with filter"""


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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.
        If 'attrs' is a list of strings, only those attributes are included.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for index in attrs:
            if index in self.__dict__:
                new_dict[index] = self.__dict__[index]
        return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        based on a given 'json' dictionary.
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
