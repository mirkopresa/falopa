# Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py)
# que pida al usuario dos números, y luego muestre el producto.


def producto(numero_1: int, numero_2: int):
    resultado = numero_1 * numero_2
    return resultado


numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

print(
    f"El resultado de la multiplicacion entre {numero_1} y {numero_2} es {producto(numero_1, numero_2)}"
)
