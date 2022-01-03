#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for filas in matrix:
        for columnas in filas:
            if columnas != filas[-1]:
                print("{:d}".format(columnas), end=' ')
            else:
                print("{:d}".format(columnas), end='')
        print("")
