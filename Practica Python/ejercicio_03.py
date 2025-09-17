# Escribir funciones que permitan
# A) Calcular el perímetro de un rectángulo dada su base y su altura.


def perimetro_rectangulo(base: int, altura: int):
    perimetro = 2 * (base + altura)
    return perimetro


resultado = perimetro_rectangulo(7, 4)
print(f"El perimetro de un rectangulo de base 7 y altura 4 es {resultado}")


# B) Calcular el área de un rectángulo dada su base y su altura.


def area_rectangulo(base: int, altura: int):
    area = base * altura
    return area


resultado = area_rectangulo(7, 4)

print(f"El area de un rectangulo de base 7 y altura 4 es {resultado}")

# C) Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
# 𝑥1, 𝑥2, 𝑦1, 𝑦2.


def area_rectangulo_v2(x_1: int, x_2: int, y_1: int, y_2: int):
    base = x_2 - x_1
    altura = y_2 - y_1
    area = base * altura
    return area


resultado = area_rectangulo_v2(3, 7, 2, 4)
print(f"El area del rectangulo es {resultado}")

# D) Calcular el perímetro de un círculo dado su radio.

import math


def perimetro_circulo(radio: int):
    perimetro = math.pi * radio * 2
    return perimetro


resultado = perimetro_circulo(4)
print(f"El perimetro del circulo de radio 4 es {resultado}")

# E) Calcular el área de un círculo dado su radio.


def area_circulo(radio: int):
    area = math.pi * (radio**2)
    return area


resultado = area_circulo(4)
print(f"El area del circulo de radio 4 es {resultado}")

# F) Calcular el volumen de una esfera dado su radio.


def volumen_esfera(radio: int):
    volumen = (4 / 3) * math.pi * (radio**3)
    return volumen


resultado = volumen_esfera(4)
print(f"El volumen de la esfera de radio 4 es {resultado}")

# G) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa


def hipotenusa(a: int, b: int):
    hipotenusa = (a**2) + (b**2)
    return hipotenusa


resultado = hipotenusa(5, 6)
print(f"La hipotenusa del triangulo de catetos 5 y 6 es {resultado}")
