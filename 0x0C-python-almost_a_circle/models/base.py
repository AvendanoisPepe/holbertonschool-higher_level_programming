#!/usr/bin/python3
"""Clase base que servira para todo el proyecto"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Obtenemos la forma de un Objeto JSON
        en forma de cadena"""
        if not list_dictionaries or list_dictionaries == [None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Crea un archivo .json con una cadena de
        bibliotecas"""
        lista = []
        if list_objs is not None and len(list_objs) > 0:
            for objeto in list_objs:
                lista.append(objeto.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as myfile:
            myfile.write(Base.to_json_string(lista))
