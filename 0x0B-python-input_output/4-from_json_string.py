#!/usr/bin/python3
"""method to return an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """converts JSON string to Python object"""

    return json.loads(my_str)
