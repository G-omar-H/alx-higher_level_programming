#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_quotion = [None] * list_length
    result = 0

    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("wrong type")
                list_quotion[i] = 0
                pass
            except ZeroDivisionError:
                print("division by 0")
                list_quotion[i] = 0
                pass
            except IndexError:
                print("out of range")
                list_quotion[i] = 0
                pass
            else:
                list_quotion[i] = result
    finally:
        return list_quotion
