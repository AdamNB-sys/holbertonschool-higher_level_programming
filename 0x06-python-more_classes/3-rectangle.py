#!/usr/bin/python3
"""this module defines a rectangle"""


class Rectangle:
    """this defines the rectangle class"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """this is the getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width and checks usage"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """this is the getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """"sets height and checks usage"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """the method to return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """this method returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """this method prints the rectangle, or empty string if 0"""
        string = ""
        if self.__width > 0:
            for i in range(self.__height):
                string += '#' * self.__width + "\n"
        return string[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
