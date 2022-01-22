#!/usr/bin/python3
"""method to write the JSON representation of an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """JSON string to text file"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
