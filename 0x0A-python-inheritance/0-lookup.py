#!/usr/bin/python3
"""returns a list of available attributes and methods of an object"""


def lookup(obj):
    """returns list of methods and attributes for object"""
    return dir(obj)
