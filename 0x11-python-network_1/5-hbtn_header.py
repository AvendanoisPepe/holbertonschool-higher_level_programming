#!/usr/bin/python3
"""Escriba una secuencia de comandos de Python que tome una URL,
envíe una solicitud a la URL y muestre el valor de la variable
X-Request-Id en el encabezado de respuesta.
"""
import requests
import sys

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get("X-Request-Id"))
