#!/usr/bin/env bash
entregado=0
total=0
entregas() {
    directory=/home/mirko/Documentos/FIUBA/2025c2/TB000/entregas/tp*
    alumnos=$(ls /home/mirko/Documentos/FIUBA/2025c2/TB000/entregas/tp1/ | wc -w)
    for entrega in $directory/*; do 
        padron=$(basename $entrega)
        tps=$(find $directory/$padron -name "tp*.py" | wc -l)
        total=$((total + 1))
        if [[ $tps -eq 2 ]]; then
            echo El alumno con padron $padron ha hecho ambas entregas.
        fi
        entregado=0
        if [[ $total -eq $alumnos ]]; then
            exit
        fi
    done
}
entregas 