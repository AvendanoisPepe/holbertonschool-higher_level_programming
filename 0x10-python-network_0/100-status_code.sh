#!/bin/bash
# Escriba un script Bash que envíe una solicitud a una URL pasada como argumento y muestre solo el código de estado de la respuesta..
curl -o /dev/null -sw "%{http_code}" "$1"
