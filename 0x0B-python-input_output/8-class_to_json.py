#!/usr/bin/python3
"""Modulo que retorna un diccionario"""


def class_to_json(obj):
    """Returna una descripcion de un diccionario"""
    return obj.__dict__
