#!/usr/bin/python3
"""module for class student"""


class Student:
    """class Student with public attributes"""
    def __init__(self, first_name, last_name, age):
        """instantiation of public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representation of Student class"""
        if type(attrs) is not list or attrs is None:
            return self.__dict__
        copy = {}
        current = self.__dict__
        for key, value in current.items():
            if key in attrs:
                copy[key] = value
        return copy

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__.update(json)
