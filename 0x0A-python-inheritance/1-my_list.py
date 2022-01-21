#!/usr/bin/python3
"""class with inheritance from list"""


class MyList(list):
    """prints a sorted list"""

    def __init__(self):
        """inherits methods and properties"""
        super().__init__()

    def print_sorted(self):
        """prints the self sorted"""
        print(sorted(self))
