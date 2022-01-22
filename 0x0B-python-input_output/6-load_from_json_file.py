#!/usr/bin/python3
"""method to create a Python object from a JSON file"""


import json


def load_from_json_file(filename):
    """converts JSON string to Python object"""

    with open(filename) as f:
        return json.loads(f.read())
