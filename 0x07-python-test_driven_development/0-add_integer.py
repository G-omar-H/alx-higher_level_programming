#!/usr/bin/pyton3
""""
add function that return the sum of two integers
"""


def add_integer(a, b=98):
    """
    proceed the addiction of two integers
    @parameters
    a: first integer
    b: second integer
    @return
        the sum of the two integers
    @exception
        TypeError if one of the two integers is not an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
