#!/usr/bin/python3
"""
module for class Square with inheritance from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class Square with inheritance from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method to print square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """returns size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and validates usage"""
        super().__init__(value, value)
