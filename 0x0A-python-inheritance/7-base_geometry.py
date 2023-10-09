#!/usr/bin/python3
"""
ALX inheritance project
"""


class BaseGeometry:
    """
    BaseGeometry first prototypes class creationg
    """

    def area(self):
        """"function that raise an exceprion error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
