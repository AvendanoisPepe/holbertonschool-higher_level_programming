#!/usr/bin/python3
"""Modulo que contiene un metodo para leer archivos"""


def read_file(filename=""):
    """Lee un archivo pasado por parametro y lo imprime"""
    with open(filename, "r", encoding="utf-8") as archivo:
        print(archivo.read())
