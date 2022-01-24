#!/usr/bin/python3
"""module adds all arguments to a Python list and saves them in a file"""


import json
import sys


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


try:
    new_list = load_from('add_item.json')
except:
    new_list = []

for c in sys.argv[1:]:
    new_list.append(c)

save_to(new_list, "add_item.json")
