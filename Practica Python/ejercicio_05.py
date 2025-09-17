# Escribir una función que, dado un número entero 𝑛, permita calcular su factorial.


def factorial(numero: int):
    factorial = 1
    for x in range(1, numero + 1):
        factorial *= x
    return factorial


resultado = factorial(5)
print(f"El factorial de 5 es {resultado}")
