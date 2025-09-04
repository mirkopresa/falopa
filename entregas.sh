#!/usr/bin/env bash
entregado=0
if [[ -z $1 ]]; then
    echo No ingresaste ningun alumno.
    exit
fi
entregas() {
    directory=/home/mirko/Documentos/FIUBA/2025c2/TB000/entregas/tp*
    for entrega in $(find $directory/$1 -name "tp*.py"); do 
        entregado=$((entregado + 1))
    done
    if [[ $entregado -eq 2 ]]; then
        echo El alumno con padron $1 ha hecho ambas entregas.
    else
        echo EL alumno con padron $1 no ha hecho ambas entregas.
    fi
}
entregas "$1"