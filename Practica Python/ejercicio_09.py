# Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
# al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
# final a obtener

from ejercicio_08 import retorno

monto = int(input("Ingrese un monto: "))
tasa = int(input("Ingrese una tasa: "))
año = int(input("Ingrese la cantidad de años: "))
resultado = round(retorno(monto, tasa, año))
print(resultado)
