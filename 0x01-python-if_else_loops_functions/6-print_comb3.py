#!/usr/bin/python3
for numerito in range(0, 9):
    for numerito2 in range(numerito + 1, 10):
        if numerito == 8:
            print("{:d}{:d}".format(numerito, numerito2))
        else:
            print("{:d}{:d}".format(numerito, numerito2), end=", ")
