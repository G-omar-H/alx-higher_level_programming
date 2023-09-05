#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number:d} is", end=" ")
nm = abs(number) % 10
if number < 0:
    print("-", end="")
if nm > 5:
    print(f"{nm:d} and is greater than 5")
elif nm == 0:
    print(f"{nm:d} and is 0")
else:
    print(f"{nm:d} and is less than 6 and not 0")
