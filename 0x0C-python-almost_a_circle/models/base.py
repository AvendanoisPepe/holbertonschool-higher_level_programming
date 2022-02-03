#!/usr/bin/python3
"""Clase base que servira para todo el proyecto"""


class Base():
    """La idea es evitar duplicidad de
    datos en las clases futuras"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inicializacion de atributos del objeto base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
