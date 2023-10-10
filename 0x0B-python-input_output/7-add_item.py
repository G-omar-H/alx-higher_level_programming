#!/usr/bin/python3
"""
ALX file I/O learning project
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys
import json

my_list = []
try:
    my_list = load_from_json_file("add_item.json")
except:
    pass
if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        my_list += sys.argv[i]
save_to_json_file(my_list, "add_item.json")
