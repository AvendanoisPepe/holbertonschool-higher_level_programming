#!/usr/bin/python3
"""Escriba una secuencia de comandos de Python que tome una URL
y un correo electrónico, envíe una solicitud POST a la URL pasada con
el correo electrónico como parámetro y muestre el cuerpo de la
respuesta (decodificado en utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        answer = response.read().decode('utf-8')
    print(answer)
