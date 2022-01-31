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
        """sets width and validates usage"""
        super().__init__(value, value)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        new = [self.id, self.size, self.x, self.y]
        print(new)
        if len(args) > 0:
            for i in range(len(args)):
                new[i] = args[i]
        else:
            for i in kwargs:
                if i == 'id':
                    new[0] = kwargs[i]
                if i == 'size':
                    new[1] = kwargs[i]
                if i == 'x':
                    new[2] = kwargs[i]
                if i == 'y':
                    new[3] = kwargs[i]
        self.__init__(
            new[1], new[2], new[3], new[0])
