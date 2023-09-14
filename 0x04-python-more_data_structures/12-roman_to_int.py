#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            if roman_string[i: i+2] == 'IX':
                num += 9
            elif roman_string[i: i+2] == 'IV':
                num += 4
            else:
                num += 1
        elif roman_string[i] == 'V' and roman_string[i-1: i+1] != 'IV':
            num += 5
        elif roman_string[i] == 'X' and roman_string[i-1: i+1] != 'IX':
            if roman_string[i: i+2] == 'XL':
                num += 40
            elif roman_string[i: i+2] == 'XC':
                num += 90
            else:
                num += 10
        elif roman_string[i] == 'L' and roman_string[i-1: i+1] != 'XL':
            num += 50
        elif roman_string[i] == 'C' and roman_string[i-1: i+1] != 'XC':
            if roman_string[i: i+2] == 'CM':
                num += 900
            elif roman_string[i: i+2] == 'CD':
                num += 400
            else:
                num += 100
        elif roman_string[i] == 'D' and roman_string[i-1: i+1] != 'CD':
            num += 500
        elif roman_string[i] == 'M' and roman_string[i-1: i+1] != 'CM':
            num += 1000
    return num
