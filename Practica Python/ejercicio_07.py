# Escribir un programa que le pida una palabra al usuario, para luego imprimirla
# 1000 veces, en una única línea, con espacios intermedios


palabra = str(input("Ingrese una palabra:\n "))
for _ in range(1000):
    print(palabra, end=" ")
