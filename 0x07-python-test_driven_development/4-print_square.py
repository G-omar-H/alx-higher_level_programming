#!/usr/bin/python3
"""
test driven devops learning project
python programing language
ALX software engineering

"""


def print_square(size):
    """
    DOES:
    print a square of '#' of size size
    @size: size of the square
    @type: integuer
    Return: void
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
