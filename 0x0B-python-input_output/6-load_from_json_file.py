#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def load_from_json_file(filename):
    """
    function that creates an object from a json file
    args:
        @filename: absolute or relative path string to a file
    Return: object decoded from json file
    """
    import json

    with open(filename, "r", encoding="UTF8") as fd:
        return json.load(fd)
