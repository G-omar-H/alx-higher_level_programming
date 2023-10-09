#!/usr/bin/python3
"""
ddefines a class and inheriance class-check
"""


def inherits_from(obj, a_class):
    """
    DOes:
        check if an object is a direct or inhrited instance fron class
    args:
        @obj: object attribute to check if instance
        @a_class: a class The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
