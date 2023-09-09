#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp1 = check_tuplen(tuple_a)
    tp2 = check_tuplen(tuple_b)
    tuple = (tp1[0] + tp2[0], tp1[1] + tp2[1])
    return tuple


def check_tuplen(tup=()):
    if len(tup) < 2:
        if len(tup) < 1:
            temp = (0, 0)
            return temp
        else:
            temp = (tup[0], 0)
            return temp
    else:
        return tup
