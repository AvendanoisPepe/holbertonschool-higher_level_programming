#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	siguiente = ((number * -1) % 10) * -1
else:
	siguiente = number % 10

if siguiente == 0:
	print("Last digit of {} is {} and is 0".format(number, siguiente))
elif siguiente > 5:
	print("Last digit of {} is {} and is greater than 5".format(number, siguiente))
elif siguiente < 6 and siguiente != 0:
	print("Last digit of {} is {} and is less than 6 and not 0".format(number, siguiente))
