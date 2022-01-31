#!/usr/bin/python3
"""
module for class Rectangle with inheritance from class Base
"""
from models.base import Base


class Rectangle(Base):
    """class for building rectangles with inheritance from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of class Rectangle"""
        if type(id) is not int and id is not None:
            raise TypeError('id must be an integer')
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """returns width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width and validates usage"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """"sets height and validates usage"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """returns x, whatever that is"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x and validates usage"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns whatever y is"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y and validates usage"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """the method to return area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """method to print the rectangle to stdout"""
        for rows in range(self.__y):
            print('')
        for cols in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """method to set the string format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attnum = 0
        att = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, att[attnum], arg)
                attnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)
