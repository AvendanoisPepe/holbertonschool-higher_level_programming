#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Devuelve un número máximo de una lista"""

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
