# Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
# al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
# final a obtener


def retorno(monto: int, tasa: int, año: int):
    total = monto * (1 + tasa / 100) ** año
    return total


monto = int(input("Ingrese un monto: "))
tasa = int(input("Ingrese una tasa: "))
año = int(input("Ingrese la cantidad de años: "))
resultado = round(retorno(monto, tasa, año))
print(resultado)
