#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    siguiente = number % 10
    print("{:d}".format(siguiente), end="")
    return (siguiente)
    