#!usr/bin/python3
"""
ALX file I/O learning project
"""


def class_to_json(obj):
    """
    function serialize disctionary description
    with simple data structure for JSOn of an object
    args:
        @obj: object instance of a class
    Return dictionary format for a JSOn serialization object
    """
    return obj.__dict__
