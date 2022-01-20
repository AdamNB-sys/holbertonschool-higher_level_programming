#!/usr/bin/python3
"""unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_values(self):
        """test for proper evaluation"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 10, 15]), 15)
        self.assertEqual(max_integer([69, 420, 1312]), 1312)
        self.assertEqual(max_integer([-10, -100, -1000]), -10)

    def test_none(self):
        """tests for none"""
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
