#!/usr/bin/python3
"""method to convert class to JSON object"""


def class_to_json(obj):
    """return dict representation"""
    return obj.__dict__
