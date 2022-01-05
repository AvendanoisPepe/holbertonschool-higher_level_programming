#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda primero: list(map(lambda segundo: segundo*segundo, primero)), matrix))
