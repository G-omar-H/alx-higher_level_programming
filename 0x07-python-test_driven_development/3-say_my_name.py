#!/usr/bin/python3
"""
test driven devops learning project
python programing language
ALX software engineering
"""


def say_my_name(first_name, last_name=""):
    """"
    DOES:
        functions to print first name last name in format:
            "My name is <first name> <last name>"
        @first_name: first name string
        @type: string
        @last_name: last name string
        @type:string
        @Return: void.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
