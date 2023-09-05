#!/usr/bin/python3
def uppercase(str):
    for i in str:
        var = ord(i)
        mod = 0
        if var >= 97 and var <= 122:
            mod = 32
        print("{}".format(chr(var - mod)), end="")
    print()
