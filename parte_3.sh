#!/usr/bin/env bash
# Ejecutar el script parte_1.sh con su propio padrón y guardar el resultado en un directorio resultado:
# ./parte_1.sh <PADRON> resultado Esto implica que no se debe modificar nada del código de parte_1.sh.

./parte_1.sh 114225 resultado 

# Ejecutar el script parte_2.sh usando el archivo generado por la parte 1 como entrada y 
# redireccionar la salida a un archivo output.txt. Esto implica que no se debe modificar 
# nada el código de parte_2.sh, sólo elegir bien la forma de usarlo / correrlo.

if [[ ! -f output.txt ]]; then
    touch output.txt
fi

cat ./resultado/resultados.txt | ./parte_2.sh > output.txt
