#!/usr/bin/python3
"""this module inherits the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class creates a square based off size"""
    def __init__(self, size):
        """instantiation of size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method to return area of the square"""
        return self.__size * self.__size
