#!/usr/bin/python3
"""Escriba un script de Python que tome sus credenciales de GitHub
(nombre de usuario y contraseña) y use la API de GitHub para mostrar
su identificación
"""
import requests
import sys

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
