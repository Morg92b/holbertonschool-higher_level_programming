#!/usr/bin/python3
"""
This is function that returns True if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    Returns: True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
