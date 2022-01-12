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

    """This calcs and returns area of the square"""
    def area(self):
        return ((self.__size) ** 2)

    """property to return size"""
    @property
    def size(self):
        return self.__size

    """this sets the size of the square"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """prints the square to stdout using #"""
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
