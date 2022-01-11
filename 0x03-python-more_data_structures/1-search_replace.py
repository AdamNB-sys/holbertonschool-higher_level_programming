#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newbie = []
    for i in my_list:
        if i == search:
            i = newbie
        newbie.append(i)
    return newbie