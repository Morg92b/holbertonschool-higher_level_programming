#!/usr/bin/python3
"""7. Load, add, save"""


import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

arguments = sys.argv[1:]

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(arguments)
save_to_json_file(items, filename)
