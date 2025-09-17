# Escribir una función que, dados cuatro números, devuelva el mayor producto de
# dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
# más grande que se puede obtener entre ellos (8 = −2 × −4)


def mayor_producto(numero_1: int, numero_2: int, numero_3: int, numero_4: int) -> int:
    lista = [numero_1, numero_2, numero_3, numero_4]
    mayor_producto = 0
    producto = 0
    for x in range(len(lista)):
        for y in range(len(lista)):
            if x != y:
                producto = lista[x] * lista[y]
            if producto > mayor_producto:
                mayor_producto = producto
    return mayor_producto


print(mayor_producto(1, 2, 10, -4))
