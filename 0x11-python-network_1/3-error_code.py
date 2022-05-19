#!/usr/bin/python3
"""Escriba un script de Python que tome una URL, envíe una solicitud
a la URL y muestre el cuerpo de la respuesta (decodificado en utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
