#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for page in sorted(a_dictionary):
        print("{}: {}".format(page, a_dictionary[page]))