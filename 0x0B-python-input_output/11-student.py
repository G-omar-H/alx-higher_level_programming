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

    def reload_from_json(self, json):
        """
        method that replaces attribute for a
        new  created class student instance
        args:
            @json:a file path that contains a
              dictionary key value refering to attributes
        return None
        """
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            elif key == "last_name":
                self.last_name = json[key]
            elif key == "age":
                self.age = json[key]
