#!/usr/bin/python3
"""this module prints first and last name"""


def say_my_name(first_name, last_name=""):
    """prints first and last name, validates format"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
