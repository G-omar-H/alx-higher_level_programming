#!/usr/bin/python3
from sys import argv
i = len(argv) - 1
if i == 0:
    print("{} arguments.".format(i))
elif i:
    j = 1
    print("{} arguments:".format(i))
    while j <= i:
        print("{}: {}".format(j, argv[j]))
        j += 1
