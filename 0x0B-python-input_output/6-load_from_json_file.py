#!/usr/bin/python3
"""Modulo que contiene el metodo
load_from_json_file"""


import json


def load_from_json_file(filename):
    """crea un objeto a base de un archivo json"""
    with open(filename, mode="r") as creOb:
        return json.load(creOb)
