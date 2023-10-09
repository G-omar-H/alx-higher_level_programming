#!/usr/bin/python3
"""ALX inheritance learning project"""


def add_attribute(obj, name, value):
    """
    function that adds an attribute if possible
    args:
        @obj: destinated class object
        @name: name of attribute
        @value: value of attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
