#!/bin/bash
# Muestra el cuerpo de la respuesta de una solicitud curl con encabezado
curl -sX "GET" -H "X-HolbertonSchool-User-Id: 98" "$1"
