#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def from_json_string(my_str):
    """
    function that deserialize a JSON representation  into  object format
    args:
        @my_obj(string): object to deserialize
        return the object format back
    """
    import json

    return json.loads(my_str)
