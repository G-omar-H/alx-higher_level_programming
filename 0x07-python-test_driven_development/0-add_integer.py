#!/usr/bin/python3
"""
    Miami
"""


def add_integer(a, b=98):
    """
        DOES
        :param a: aaaaa
        :type a: aaa
        :param b: bbbbb
        :type b: bbbb
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
