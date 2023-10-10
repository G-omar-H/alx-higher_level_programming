#!/usr/bin/python3
"""
ALX file I/O learning project
"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""
function that writes the Json representation of an object  into a file
args:
    @my_obj: object to serialize as Json
    @filename: absolute or relative path to the file
    Return: None
"""
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""
function that creates an object from a json file
args:
    @filename: absolute or relative path string to a file
Return: object decoded from json file
    """
import sys

"""
The sys module in Python provides various functions and variables 
that are used to manipulate different parts of the Python runtime environment. 
It allows operating on the interpreter 
as it provides access to the variables and functions 
that interact strongly with the interpreter
"""
import json

"""
json serialization module
lightweight data interchange format inspired by JavaScript object literal syntax (
    although it is not a strict subset of JavaScript 1 ).
"""

my_list = []
try:
    my_list = load_from_json_file("add_item.json")
except:
    pass
if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        my_list += sys.argv[i]
save_to_json_file(my_list, "add_item.json")
