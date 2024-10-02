#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize 'data' to JSON format and save it to 'filename'.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load data from 'filename' and deserialize it from JSON to Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
