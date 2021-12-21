#!/usr/bin/python3
def uppercase(str):
    for numerito in str:
        if ord(numerito) >= ord('a') and ord(numerito) <= ord('z'):
            charsito = chr(ord(numerito) - 32)
        else:
            charsito = numerito
        print("{:s}".format(charsito), end="")
    print("")
