#!/usr/bin/python3
"""Technical intervieaw"""

def pascal_triangle(n):
    """
    function that creat a  pascal triangle of n
    args:
        @n: integuer representing the pascal's triangle
    Return pascal triangle of n
    """
    my_list = []
    for i in range(1, n + 1):
       my_list += [i + j for j in range(i)]
    print(my_list)
    