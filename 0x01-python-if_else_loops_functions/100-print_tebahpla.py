#!/usr/bin/python3
for numerito in range(ord('z'), ord('a') -1, -1):
    if numerito % 2 != 0:
        numerito = numerito - 32
    print("{:c}".format(numerito), end="")
