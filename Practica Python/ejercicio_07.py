# Escribir un programa que le pida una palabra al usuario, para luego imprimirla
# 1000 veces, en una única línea, con espacios intermedios


contador = 0
palabra = str(input("Ingrese una palabra:\n "))
while contador != 1000:
    contador += 1
    print(palabra, end=" ")
