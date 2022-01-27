#!/usr/bin/python3
"""
module for class Base to be
the base for all classes in this project
"""


class Base:
    """class to build project classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of the Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
