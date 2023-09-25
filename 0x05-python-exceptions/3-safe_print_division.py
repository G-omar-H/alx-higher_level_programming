#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result:", end=" ")
    except ZeroDivisionError:
        result = None
        print("Inside result:", end=" ")
    finally:
        print("{}".format(result))
        return result
