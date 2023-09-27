#!/usr/bin/python3
"""defining a square by size"""


class Square:
    """square classe creating
    Attributes:
        size (int): private attribute defining the square size
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
