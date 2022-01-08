#!/usr/bin/env python3
def no_c(my_string):
    newstring = my_string.translate({ord(c): None for c in "Cc"})
    return newstring
