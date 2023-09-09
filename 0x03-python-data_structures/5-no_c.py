#!/usr/bin/python3
def no_c(my_string):
    temp = my_string.translate({ord('c'): None})
    new_string = temp.translate({ord('C'): None})
    return new_string
