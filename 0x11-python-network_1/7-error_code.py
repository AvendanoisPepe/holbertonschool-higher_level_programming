#!/usr/bin/python3
"""Escriba un script de Python que tome una URL, envíe una
solicitud a la URL y muestre el cuerpo de la respuesta.
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    print(r.text) if status < 400 else print(
        "Error code: {}".format(r.status_code))
