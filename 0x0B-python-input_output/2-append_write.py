#!/usr/bin/python3
"""module to append a string to the end of a file"""


def append_write(filename="", text=""):
    """appends text to filename"""
    with open(filename, 'a', encoding = 'utf-8') as f:
        return f.write(text)
