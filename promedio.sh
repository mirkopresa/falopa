#!/usr/bin/env bash
tp1_nota=5
tp2_nota=7
if (("($tp1_nota + $tp2_nota)" / 2 >= 7 )); then
    echo "Aprobaste!"
    exit
else
    echo "Desaprobaste."
fi