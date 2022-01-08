#!/usr/bin/env python3


def no_c(my_string):
    newstring = my_string.translate({ord(x): None for x in "Cc"})
    return newstring
