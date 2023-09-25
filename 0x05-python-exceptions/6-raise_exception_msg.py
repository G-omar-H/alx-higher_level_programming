#!/usr/bin/python3
class Messageprompt(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def raise_exception_msg(message=""):
    raise Messageprompt(message)
