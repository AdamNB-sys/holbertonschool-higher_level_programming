#!/usr/bin/python3
"""
module for class Rectangle with inheritance from class Base
"""
from models.base import Base


class Rectangle(Base):
    """class for building rectangles with inheritance from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of class Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # def att_checker(self, blah blah blah )
