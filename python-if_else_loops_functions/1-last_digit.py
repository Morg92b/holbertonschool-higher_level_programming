#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10
last_digit2 = number % -10

if number >= 0:
    lasd = last_digit
else:
    lasd = last_digit2

print(f"Last digit of {number} is {lasd}", end=" ")

if lasd > 5:
    print("and is greater than 5")
elif lasd == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
