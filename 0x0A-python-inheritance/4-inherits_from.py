#!/usr/bin/python3
"""module checks to see if object is instance of an inherited class"""


def inherits_from(obj, a_class):
    """returns True if object is instance of inherited class"""

    return (issubclass(type(obj), a_class))
