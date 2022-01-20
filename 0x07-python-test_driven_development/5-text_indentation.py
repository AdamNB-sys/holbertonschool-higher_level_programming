#!/usr/bin/python3
"""prints text formatted with newlines after certain chars"""


def text_indentation(text):
    """prints text with two newlines after each . ? :, and checks for usage"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    
    newliners = ['.', '?', ':']
    marker = False

    for c in text:
        if marker:
            if c == ' ':
                continue
            marker = False
        if c in newliners:
            print(c)
            print()
            marker = True
        else:
            print(c, end='')
