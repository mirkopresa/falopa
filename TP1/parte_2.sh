#!/usr/bin/env bash
# Se leera de stdin nombres de pokemons y se mostrará por stdout cierta informacion de los mismos:
# Nombre
# Peso
# Altura
# Habilidades
pokemons_path=$(find . -name pokemon.csv)
abilities_id_path=$(find . -name pokemon_abilities.csv)
abilities_name_path=$(find . -name ability_names.csv)
while IFS= read -r line; do

    name=$(grep -Ei ".*,$line," $pokemons_path | cut -d "," -f 2)
    weight=$(grep -Ei ".*,$line," $pokemons_path | cut -d "," -f 4)
    height=$(grep -Ei ".*,$line," $pokemons_path | cut -d "," -f 5)
    echo "-------------------------------------------------------"
    echo El nombre del pokemon es: "${name^}"
    echo El peso de "${name^}" es: $weight
    echo La altura de "${name^}" es: $height
    echo "-------------------------------------------------------"

    pokemon_id=$(grep -Ei ".*,$line," $pokemons_path | cut -d "," -f 1)
    abilities_id=$(grep -Ei "^$pokemon_id," $abilities_id_path | cut -d "," -f 2)
    echo Sus habilidades son:
    for ability_id in $abilities_id; do
        ability_name=$(grep -Ei "^$ability_id,7,*" $abilities_name_path | cut -d "," -f 3) # 7 por idioma español
        echo - $ability_name
    done
    echo -e "-------------------------------------------------------\\n"

done < "${file:-/dev/stdin}" # Lee de stdin