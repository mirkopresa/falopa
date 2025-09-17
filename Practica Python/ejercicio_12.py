# A) Escribir una función que dado un número entero devuelva 1 si el mismo
# es impar y 0 si fuera par.


def par_impar(numero: int) -> int:
    if (numero % 2) == 0:
        return 0
    else:
        return 1


# B) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y
# 1 si fuera par


def impar_par(numero: int) -> int:
    if (numero % 2) == 0:
        return 1
    else:
        return 0


# C) Escribir una función que dado un número entero devuelva el dígito de las unidades.
# Por ejemplo, para 153 debe devolver 3.


def digito(numero: int) -> int:
    contador = 0
    while round(numero) != 0:
        contador += 1
        numero /= 10
    return contador


# D) Escribir una función que dado un número devuelva el primer número múltiplo de 10
# inferior a él. Por ejemplo, para 153 debe devolver 150.


def primer_multiplo(numero: int):
    contador = 0
    while numero > 10:
        contador += 10
        numero -= 10
    return contador


resultado = par_impar(3)
print(resultado)

resultado = impar_par(3)
print(resultado)

resultado = digito(153)
print(resultado)

resultado = primer_multiplo(153)
print(resultado)
