#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number:d}", end=" ")
number = number % 10
if number > 5:
    print(f"is {number:d} and is greater than 5")
elif number == 0:
    print(f"is {number:d} and is 0")
else:
    print(f"is {number:d} and is less than 6 and not 0")
