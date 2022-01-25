#!/usr/bin/python3
"""module for class student"""


class Student:
    """class Student with public attributes"""
    def __init__(self, first_name, last_name, age):
        """instantiation of public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict representation of Student class"""
        return self.__dict__
