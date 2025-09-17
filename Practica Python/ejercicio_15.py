# Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
# a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
# el resultado junto con el número de orden correspondiente.


def factorial(numero: int):
    factorial = 1
    for x in range(1, numero + 1):
        factorial *= x
    return factorial


cantidad = int(input("Ingrese un numero: "))
for x in range(0, cantidad + 1):
    resultado = factorial(x)
    print(f"{resultado} - {x}")
