#!/usr/bin/python3
"""
ALX file I/O learning project
"""
import sys

if __name__ == "__main__":
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
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
