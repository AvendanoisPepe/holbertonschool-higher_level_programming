#!/usr/bin/python3
"""Modulo que cumple con escribir un objeto en
un archivo txt con una representacion JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Funcion que escribe un objeto en un documento
    de texto"""
    with open(filename, mode="w", encoding="utf-8") as jeison:
        jeison.write(json.dumps(my_obj))
