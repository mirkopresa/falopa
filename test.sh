#!/usr/bin/env bash
while IFS= read -r linea; do
    echo $linea
done < "$file"