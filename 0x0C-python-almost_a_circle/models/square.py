#!/usr/bin/python3
"""
module for class Square with inheritance from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square with inheritance from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization of class Square"""
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
        """sets size and validates usage"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attnum = 0
        att = ['id', 'size', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, att[attnum], arg)
                attnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)
