#!/usr/bin/python3
"""Modulo que escribe una cadena en
cierto archivo de texto
"""


def write_file(filename="", text=""):
    """Escribe una cadena en filename y
    returna la cantidad de carcateres"""
    with open(filename, mode="w", encoding="utf-8") as nuevoArchivo:
        return nuevoArchivo.write(text)
