#!/usr/bin/python3
for numerito in range(ord("a"), ord("z") + 1):
    if numerito != 101 and numerito != 113:
        print("{:c}".format(numerito), end="")