#!/usr/bin/python3
"""Unittesting for the Square module/class
Tests are done for each method of the class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestClassSquare(unittest.TestCase):
    """Test class for testing Square class"""

    def test_id(self):
        """
        Test that the id of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.id, 2)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.id, 12)

    def test_width(self):
        """
        Test that the width of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        s2 = Square(10, 0, 0, 12)

    def test_height(self):
        """
        Test that the height of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.height, 10)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.height, 10)

    def test_x(self):
        """
        Test that the x of the square is correct
        """
        s1 = Square(10)
        self.assertEqual(s1.x, 0)
        s2 = Square(10, 0, 0, 12)
        self.assertEqual(s2.x, 0)
