#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    _list = []
    for x in set_1:
        if x not in set_2:
            _list.append(x)
    for x in set_2:
        if x not in set_1:
            _list.append(x)
    _set = set(_list)
    return _set
