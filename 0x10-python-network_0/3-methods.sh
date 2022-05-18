#!/bin/bash
# muestra los metodos http
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
