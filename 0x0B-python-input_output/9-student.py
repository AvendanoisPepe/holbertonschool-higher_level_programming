#!/usr/bin/python3
"""Modulo estudiante"""


class Student():
    """Se crea la clase estudian y se define"""

    def __init__(self, first_name, last_name, age):
        """Instanciacion"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returna una representacion en diccionario"""
        return self.__dict__
