#!/usr/bin/python3
"""Escriba un script de Python que tome una URL y una dirección de
correo electrónico, envíe una solicitud POST a la URL pasada con el
correo electrónico como parámetro y, finalmente, muestre el cuerpo
de la respuesta.
"""
import requests
import sys

if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
