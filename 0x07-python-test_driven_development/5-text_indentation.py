#!/usr/bin/python3
"""
test driven devops learning project
python programing language
ALX software engineering

"""


def text_indentation(text):
    """function that prints a text"""

    i = 0

    if type(text) != str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])
    print(text, end="")
