#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    var = 0
    item = ""
    for key, value in a_dictionary.items():
        if value > var:
            var = value
            item = key
    return item
