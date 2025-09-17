# Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
# número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
# C x ( 1 + X / 100)^n


def retorno(monto: int, tasa: int, año: int):
    total = monto * (1 + tasa / 100) ** año
    return total


print(retorno(300000, 50, 4))
