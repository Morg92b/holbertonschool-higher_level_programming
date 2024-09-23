#!/usr/bin/python3
"""
This is a function that returns True
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns: True if obj is an instance or inherited instance of a_class,
    False otherwise.
    """
    return type(obj) is a_class
