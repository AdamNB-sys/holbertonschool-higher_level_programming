#!/usr/bin/python3
"""module to write string to text file and return # chars appended"""


def write_file(filename="", text=""):
    """writes string to text file"""

    with open(filename, 'w', encoding = 'utf-8') as f:
        return f.write(text)
