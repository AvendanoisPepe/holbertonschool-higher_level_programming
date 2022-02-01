#!/usr/bin/python3
"""Modulo que returna un json en cadena"""
import json


def to_json_string(my_obj):
    """Metodo"""
    return json.dumps(my_obj)
