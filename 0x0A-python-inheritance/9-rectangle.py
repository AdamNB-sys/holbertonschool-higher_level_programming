#!/usr/bin/python3
"""this module inherits the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry and integer validator"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method to return area of the object"""
        return self.__width * self.__height

    def __str__(self):
        """returns description of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
