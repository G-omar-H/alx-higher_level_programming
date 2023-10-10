#!/usr/bin/python3
"""
    File I/O ALX learning project
"""


def read_file(filename=""):
    """
    function that open and reads a file to print it's content into stdout
    args:
        @filename(string): absolute or relative path to the file
        Return: void
    """
    with open(filename, "r", encoding="UTF8") as fd:
        for line in fd:
            print(line)
