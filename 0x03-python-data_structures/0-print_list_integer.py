#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        if len(my_list):
            i = 0
            while i < len(my_list):
                print(f"{my_list[i]}")
                i += 1
