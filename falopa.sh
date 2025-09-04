#!/usr/bin/env bash
directory=/home/mirko/Documentos/FIUBA/2025c2
max=0
mat=0
for materia in "$directory"/*; do 
    ejercicios=$(find $materia \( -name "ej*.py" -o -name "ej*.doc" \) | wc -w)
    if [[ $ejercicios -gt $max ]]; then
        max=$ejercicios
        mat=$(basename $materia)
    fi
done
if [[ $mat ! "nada" ]]; then
    echo "La materia mas practicada es $mat con una cantidad de $max ejercicios."
else 
    echo "sos tremendo vago"
fi