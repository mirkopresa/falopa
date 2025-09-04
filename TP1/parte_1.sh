#!/usr/bin/env bash
# Este script precisa filtrar y obtener nombres de ciertos Pokemons
# Debe recibir por parametro un padron/legajo y un nombre de un directorio
# donde guardar un archivo llamado resultado.txt
# En caso de no existir el directorio, el script debe crearlo y almacenarlo 
# Y en caso de resultados.txt ya existir, guardarlo en el directorio
parte_1() {

    if [[ $1 == "" || $2 == "" ]]; then # Chequea si ingrese un padron o directorio, y si no, quitea
        echo No ingresaste nada.
        exit
    fi 

    if [[ ! -d $2 ]]; then # Crea el directorio si no existe
        mkdir $2
    fi

    if [[ -e "$2"/"resultados.txt" ]]; then # Si resultado.txt ya existia, lo sobreescribe
        touch "$2"/resultados.txt > "$2"/resultados.txt
    else
        touch "$2"/resultados.txt # Crea resultado.txt si no existia
    fi

    tipo_id_pokemon=$(( $1 % 18 + 1 ))
    estadisticas=$(( $1 % 100 + 350 ))
    type_path=$(find . -name pokemon_types.csv) 
    stats_path=$(find . -name pokemon_stats.csv)
    pokemons_path=$(find . -name pokemon.csv)
    pokemon_type_id=$(grep -Ei ".*,$tipo_id_pokemon,*" $type_path | cut -d "," -f 1)

    for id in $pokemon_type_id; do # Este for suma stat por stat las stats de cada pokemon
        total_stats=0
        stat=$(grep -Ei "^$id," $stats_path | cut -d "," -f 3)
        for numero in $stat; do
        total_stats=$(( total_stats + numero ))
        done
        if [[ $total_stats > $estadisticas ]]; then # Y si son mayores a la variable estadistica, lo guarda en resultados.txt
            pokemon=$(grep -Ei "^$id," $pokemons_path | cut -d "," -f 2)
            echo $pokemon >> "$2"/resultados.txt # echo El pokemon es $pokemon y su stat total es $total_stats y su tipo es $tipo_id_pokemon >> "$2"/resultados.txt sirve para chequear que funciona bien
        fi
    done

}

parte_1 "$@" # Esto recibe el padron primero, y despues deberia recibir el directorio