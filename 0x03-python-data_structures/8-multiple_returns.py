#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence):
        tup = (len(sentence), sentence[0])
    else:
        tup = (len(sentence), None)
    return tup
