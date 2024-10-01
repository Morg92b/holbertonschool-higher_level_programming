#!/usr/bin/python3
"""4. JSON string"""


import json


def from_json_string(my_str):
    """this function that returns an object represented by a JSON string"""
    return json.loads(my_str)
