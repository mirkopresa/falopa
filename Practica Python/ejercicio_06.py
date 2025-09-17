# Escribir funciones que resuelvan los siguientes problemas:

# A) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.


def calculadoraloca(numero_1: int, numero_2: int):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    return suma, resta, division, multiplicacion


resultado = calculadoraloca(4, 5)
print(
    f"La suma de 4 y 5 es {resultado[0]}, su resta es {resultado[1]}, su division es {resultado[2]} y su multiplicacion es {resultado[3]}"
)

# B) Dado un número natural 𝑛, imprimir su tabla de multiplicar


def tabla_multiplicar(numero: int):
    for x in range(0, 10 + 1):
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")


tabla_multiplicar(5)
