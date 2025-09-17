# Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))
if numero_1 < numero_2:
    for x in range(numero_1, numero_2 + 1):
        if x % 2 == 0:
            print(x)
else:
    for x in range(numero_2, numero_1 + 1):
        if x % 2 == 0:
            print(x)
