#!/usr/bin/python3
"""Agrega una cadena de texto y returna
el numero de caracteres añadidos"""


def append_write(filename="", text=""):
    """Agrega una cadena al final del archivo"""
    with open(filename, mode="a", encoding="utf-8") as finalLinea:
        return finalLinea.write(text)
