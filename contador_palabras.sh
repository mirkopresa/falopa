#!/usr/bin/env bash

# Contar la cantidad de palabras de un archivo sin usar wc.
cantidad=0
if [[ ! -e $1 ]]; then
    echo "El archivo $1 no existe"
    exit 
fi
while IFS= read -r linea; do
    for palabra in $linea; do 
        cantidad=$((cantidad + 1))
        done
done < "$1"
echo $cantidad