#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    for JSON serialization of an object.
    """
    return obj.__dict__
