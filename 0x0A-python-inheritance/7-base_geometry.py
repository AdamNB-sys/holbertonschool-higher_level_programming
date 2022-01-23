#!/usr/bin/python3
"""module for class BaseGeometry"""


class BaseGeometry:
    """the class for BaseGeometry"""
    def area(self):
        """raises exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates usage of name and value"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
