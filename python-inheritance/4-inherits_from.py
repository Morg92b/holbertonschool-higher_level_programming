#!/usr/bin/python3
"""
Function to check if an object inherits from a class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that 
    inherited (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
