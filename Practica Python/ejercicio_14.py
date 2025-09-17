# Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los
# primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen
# mediante la suma de los números naturales desde 1 hasta 𝑛. Es decir, si se piden los primeros 5
# números triangulares, el programa debe imprimir:
# 1 - 1
# 2 - 3
# 3 - 6
# 4 - 10
# 5 - 15

numero = int(input("Ingrese un numero: "))
resultado = 0

for x in range(1, numero + 1):
    resultado += x
    print(f"{x} - {resultado}")

# otra manera 
"""
for x in range(1, numero + 1):
    resultado = x * (x + 1) / 2
    print(f"{x} - {round(resultado)}")
"""
