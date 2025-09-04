#!/usr/bin/env bash
sorted=($(ls -1 | sort -d))
n=${#sorted[@]}
if [[ $(( $n % 2 )) == 0 ]]; then
    num=$(((n - 1) / 2))
else
    num=$((n / 2))
fi
echo ${sorted[$num]}
