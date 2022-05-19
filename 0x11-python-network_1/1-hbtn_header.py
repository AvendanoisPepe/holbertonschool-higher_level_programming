#!/usr/bin/python3
"""Escriba una secuencia de comandos de Python que tome una URL,
envíe una solicitud a la URL y muestre el valor de la variable
X-Request-Id que se encuentra en el encabezado de la respuesta.
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
