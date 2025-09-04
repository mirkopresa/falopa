#!/usr/bin/env bash
promedio() {
    total=0
    cantidad="$#"
    for notas in $@; do
        total=$((total + notas))
    done
    prom=$((total / cantidad))
    if [[ $prom -ge 7 ]]; then
        echo Aprobaste con un promedio de $prom
    else
        echo Desaprobaste con un promedio de $prom
    fi
}
promedio "$@"
