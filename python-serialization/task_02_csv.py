#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.
    Returns True if successful, False if the CSV file is not found.
    """
    try:
        with open(csv_filename, 'r') as file:
            csvReader = csv.DictReader(file)
            rows = list(csvReader)

        with open("data.json", "w") as json_file:
            json.dump(rows, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
