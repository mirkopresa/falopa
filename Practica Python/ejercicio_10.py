# Escribir una función que convierta un valor dado en grados Fahrenheit a grados
# Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32


def conversor(temp: int) -> int:
    convertida = (9 / 5 * temp) + 32
    return convertida


print(conversor(32))
