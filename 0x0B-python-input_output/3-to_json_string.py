#!/usr/bin/python3
"""module to return the JSON string representation of a Python object"""


import json


def to_json_string(my_obj):
    """returns JSON version of an object"""

    return json.dumps(my_obj)
