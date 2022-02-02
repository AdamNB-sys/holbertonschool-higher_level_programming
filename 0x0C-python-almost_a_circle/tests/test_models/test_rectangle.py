#!/usr/bin/python3
"""Unittesting for the Rectangle module/class
Tests are done for each method of the class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models import rectangle
import inspect
import pep8


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class' style and documentation"""
