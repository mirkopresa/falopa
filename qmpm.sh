#!/usr/bin/env bash
directory="/Documentos/FIUBA/2025c2"
iterate() {
    local dir="$1"
    for subdir in $dir; do
        if [[ -d $subdir ]]; then
            ejercicios= find $subdir -name "ej*.py"
        fi
        if [[ -e $ejercicios ]]; then
            ej=$((ej + 1 ))
        fi
    done  
    echo $ej
}
iterate "$directory"
