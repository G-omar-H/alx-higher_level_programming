#!/usr/bin/python3
"""ALX inheritance learning project"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    square class inheriting from Rectangle parents attributes
    """

    def __init__(self, size):
        """
        class initializating...
        args:
            @size: integuer square size reprezentation
            @type: int
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
