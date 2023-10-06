#!/usr/bin/pyton3
""""add function that return the sum of two integers"""


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
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
