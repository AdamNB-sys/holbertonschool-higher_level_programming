#!/usr/bin/python3
"""this module reads a text file and returns it to stdout"""


def read_file(filename=""):
    """reads file and prints to stdout"""

    with open(filename, encoding = 'utf-8') as f:
        print(f.read(), end="")
