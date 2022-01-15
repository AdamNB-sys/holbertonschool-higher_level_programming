#!/usr/bin/python3
"""
add_integer:
    returns the sum of two ints or floats as an int
    """


def add_integer(a, b=98):
    """
    takes two numbers, either int or float, and adds them, 
    returning an int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be integer')
    return int(a) + int(b)
