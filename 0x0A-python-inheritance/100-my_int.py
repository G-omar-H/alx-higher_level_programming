#!/usr/bin/python3
"""
ALX inheritance learning project
"""


class MyInt(int):
    """
    subclass that inherit attribute from int parent class
    """

    def __init__(self, integer):
        """initialize class"""
        self.integer = integer

    def __eq__(self, value):
        """override == operator into !="""
        return self.integer != value

    def __ne__(self, value):
        """"override != operator to =="""
        return self.integer == value
