#!/usr/bin/python3
"""Unittesting for the Rectangle module/class
Tests are done for each method of the class"""


import inspect
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import pep8
import json
import os


class TestBaseClass(unittest.TestCase):
    """
    Test Base Class
    """

    def test_module_docstring(self):
        """
        Tests for the module docstring
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests for the presence of docstrings in all functions
        """
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
