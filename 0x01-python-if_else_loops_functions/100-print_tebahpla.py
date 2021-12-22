#!/usr/bin/python3
for numerito in range(ord("z"), ord("a"), -1):
    if numerito % 2 == 0:
        print("{}".format(chr(numerito)), end="")
    else:
        print("{}".format(chr(numerito - 32)), end="")