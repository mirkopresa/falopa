# Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario
# dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
# por pantalla la duración total en horas, minutos y segundos.


def segundos(tiempo_1: str, tiempo_2: str) -> int:
    hora_1, minutos_1, segundos_1 = tiempo_1.split(":")
    hora_2, minutos_2, segundos_2 = tiempo_2.split(":")
    hora_total = (int(hora_1) + int(hora_2)) * 3600
    minutos_total = (int(minutos_1) + int(minutos_2)) * 60
    segundos_total = int(segundos_1) + int(segundos_2) + hora_total + minutos_total
    return segundos_total


def intervalo(tiempo: int) -> str:
    horas = 0
    minutos = 0
    segundos = 0
    while tiempo >= 3600:
        horas += 1
        tiempo -= 3600
    while tiempo >= 60:
        minutos += 1
        tiempo -= 60
    segundos = tiempo
    intervalo = f"{horas:02}:{minutos:02}:{segundos:02}"
    return intervalo


pb_1 = str(input("Ingrese un tiempo en formato HH:MM:SS: "))
pb_2 = str(input("Ingrese otro tiempo en formato HH:MM:SS: "))

suma_segundos = segundos(pb_1, pb_2)
suma_total = intervalo(suma_segundos)
print(suma_total)
