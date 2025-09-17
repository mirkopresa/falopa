# Escribir un programa que utilice la función anterior para generar una tabla de
# conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10

for x in range(0, 120 + 1, 10):
    convertida = (x - 32) * (5 / 9)
    print(f"{x}°F = {round(convertida)}°C")
