#!/usr/bin/python3
"""This class defines the size of a square"""


class Square:
    """class square with a private size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
