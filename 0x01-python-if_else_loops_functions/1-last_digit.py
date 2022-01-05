#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
string = "Last digit of"
less = "is less than 6 and not 0"
if number < 0:
    last = last * -1
if last > 5:
    print("{} {} is {} and is greater than 5".format(string, number, last))
elif last == 0:
    print("{} {} is {} and is 0".format(string, number, last))
elif last < 6 and last != 0:
    print("{} {} is {} and {}".format(string, number, last, less))