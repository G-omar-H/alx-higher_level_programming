#!/usr/bin/python3
def no_c(my_string):
    i = 0
    #while i < len(my_string):
     #       if my_string[i]  not in  ['c', 'C']:
     #          new_string + my_string[i]
     #    new_string = my_string for my_string[i] not in ['c', 'C']
    return my_string.translate(delete='cC')
