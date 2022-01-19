import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_isempty(self):
        """test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test

if __name__ == '__main__':
    unittest.main()
