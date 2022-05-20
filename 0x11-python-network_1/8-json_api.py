#!/usr/bin/python3
"""Escriba un script de Python que reciba una carta y envíe
una solicitud POST a http://0.0.0.0:5000/search_user con la carta
como parámetro.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]
    url = requests.post('http://0.0.0.0:5000/search_user', data={'q': value})
    try:
        urls = url.json()
        if len(url) == 0:
            print("No result")
        else:
            print("[{}] {}".format(url["id"], url["name"]))
    except Exception as error:
        print("Not a valid JSON")
