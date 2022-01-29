#!/usr/bin/python3
"""
module for class Square with inheritance from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class Square with inheritance from Rectangle"""
