#!/usr/bin/python3
"""prints a square of # chars based on size"""


def print_square(size):
    """prints a square, validating usage"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for square in range(size):
        print(size * '#')
