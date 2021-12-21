#!/usr/bin/python3
for numerito in range(0, 99 + 1):
    if numerito == 99:
        print("{:d}".format(numerito))
    else:
        print("{:02d}".format(numerito), end=", ")
