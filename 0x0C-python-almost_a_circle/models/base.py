#!/usr/bin/python3
"""Almost cycle Alx learnirng project"""


class Base:
    """
    base class for the upcoming project...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        Base.__nb_objects += 1
        if id == None:
            self.id = Base.__nb_objects
