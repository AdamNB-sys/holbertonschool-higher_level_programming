#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highScore = 0
        for key, value in a_dictionary.items():
            if value > highScore:
                highScore, newkey = value, key
        return newkey
