#!/usr/bin/python3
"""
ALX file I/O learning project
"""


class Student:
    """
    student class that defines student by:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        """
        class initialization...
        public attributes:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        class mehtod that retrieves a dictionary representation
        of a Student instance
        """
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
