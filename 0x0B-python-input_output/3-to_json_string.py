#!/usr/bin/python3
"""
ALX file I/O learning project
"""


def to_json_string(my_obj):
    """
    function that serialize an  object into json format
    args:
        @my_obj(string): object to serialize
        return json representation of the object
    """
    import json

    return json.dumps(my_obj)
