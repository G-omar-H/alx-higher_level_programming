#!/usr/bin/python3
"""Inherit the class"""


def is_same_class(obj, a_class):
    """
    check if obj is an instance of a given class
    """
    if type(obj) == a_class:
        return True
    return False
