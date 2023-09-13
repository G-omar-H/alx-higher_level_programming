#!/usr/bin/python3
def common_elements(set_1, set_2):
    _set = set()
    _list = []
    for item in set_1:
        for item2 in set_2:
            if item == item2:
                _list += item
    _list = set(_list)
    return _list
