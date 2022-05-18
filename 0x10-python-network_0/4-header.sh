#!/bin/bash
# Muestra el cuerpo de la respuesta de una solicitud curl con encabezado
curl -sX "GET" -H "X-School-User-Id: 98" "$1"
