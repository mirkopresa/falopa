# Modificar el programa anterior para que pueda generar fichas de un juego que
# puede tener números de 0 a n

n = int(input("Ingrese un numero: "))

for x in range(n, -1, -1):
    for y in range(0, x + 1, 1):
        print(f"{x}-{y}")
