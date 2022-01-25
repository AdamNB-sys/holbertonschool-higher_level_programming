#!/usr/bin/python3
"""method to convert class to JSON object"""


def class_to_json(obj):
    """returns the objects writable attributes"""
    return obj.__dict__
