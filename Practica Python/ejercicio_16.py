# Escribir un programa que imprima por pantalla todas las fichas de dominó, de
# una por línea y sin repetir.

for x in range(6, -1, -1):
    for y in range(0, x + 1, 1):
        print(f"{x}-{y}")
