# Escribir funciones que resuelvan los siguientes problemas:

# A) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.


def calculadoraloca(numero_1: int, numero_2: int) -> None:
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1 / numero_2
    multiplicacion = numero_1 * numero_2
    print(
        f"La suma de 4 y 5 es {suma}, su resta es {resta}, su division es {division} y su multiplicacion es {multiplicacion}"
    )


# B) Dado un número natural 𝑛, imprimir su tabla de multiplicar


def tabla_multiplicar(numero: int) -> None:
    for x in range(0, 10 + 1):
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")


calculadoraloca(4, 5)
tabla_multiplicar(5)
