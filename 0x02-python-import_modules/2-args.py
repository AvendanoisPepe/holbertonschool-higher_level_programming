#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numerito = len(sys.argv)    
    if numerito == 1:
        print("{} arguments.".format(numerito - 1))
    elif numerito == 2:
        print("{} arguments:".format(numerito - 1))
    else:
        print("{} arguments: ".format(numerito - 1))

    for iterador in range(1, numerito):
        print("{}: {}".format(iterador, sys.argv[iterador]))
