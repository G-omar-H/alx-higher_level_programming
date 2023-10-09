#!usr/bin/python3
"""Class inheritance"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance or inherit instance of a given class
    """
    if isinstance(obj, a_class):
        return True
    return False
