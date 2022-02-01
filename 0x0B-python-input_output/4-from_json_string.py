#!/usr/bin/python3
"""Modulo que contiene un metodo que retorna una
cadena json a base de un objeto"""
import json


def from_json_string(my_str):
    """Returna un objeto de python con
    una representacion de una cadena json"""
    return json.loads(my_str)
