#!/usr/bin/python3
"""Modulo estudiante"""


class Student():
    """Se crea la clase estudian y se define"""

    def __init__(self, first_name, last_name, age):
        """Instanciacion"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returna una representacion en diccionario"""
        diccionario = dict()
        if attrs is None:
            return self.__dict__
        else:
            for iterador in attrs:
                if iterador in self.__dict__:
                    diccionario[iterador] = self.__dict__[iterador]
            return (diccionario)
