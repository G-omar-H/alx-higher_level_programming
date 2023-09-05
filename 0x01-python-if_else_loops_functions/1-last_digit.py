#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10 if number > 0 else number % -10
print("Last digit of {} is {} and is".format(number, mod), end=" ")
if mod == 0:
    print("0")
elif mod > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0", end="\n")
