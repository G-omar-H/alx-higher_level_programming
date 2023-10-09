#!/usr/bin/python3
"""
ALX inhritence project
"""


class MyList(list):
    """Implemets sorted printing for the built=in list class"""

    def print_sorted(self):
        """prints a list in sorted ascending order"""
        print(sorted(self))
