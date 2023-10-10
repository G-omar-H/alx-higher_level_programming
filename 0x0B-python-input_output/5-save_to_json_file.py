#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes the Json representation of an object  into a file
    args:
        @my_obj: object to serialize as Json
        @filename: absolute or relative path to the file
        Return: None
    """
    import json

    with open(filename, "w", encoding="UTF8") as fd:
        fd.write(json.dumps(my_obj))
