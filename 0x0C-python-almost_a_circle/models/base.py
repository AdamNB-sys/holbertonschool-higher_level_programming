#!/usr/bin/python3
"""
module for class Base to be
the base for all classes in this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts class dictionaries to JSON string"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves JSON representaion of dictionary to a file"""
        if len(list_objs) < 1 or list_objs is None:
            return []
        filename = cls.__name__ + '.json'
        copy = []
        for i in list_objs:
            copy.append(i.to_dictionary())
        with open(filename, 'w') as f:
            f.write(json.dumps(copy))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation"""
        if len(json_string) < 1 or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a constructed class from dictionary"""
        if cls.__name__ == 'Rectangle':
            copy = cls(1, 1, 0, 0)
        else:
            copy = cls(1, 0, 0)
        copy.update(**dictionary)
        return copy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = cls.__name__ + '.json'
        copy = []
        try:
            with open(filename, 'r') as f:
                for ob in cls.from_json_string(f.read()):
                    copy.append(cls.create(**ob))
            return copy
        except Exception:
            return []
