# Escribir dos funciones que permitan calcular:
# A) La duración en segundos de un intervalo dado en horas, minutos y segundos.


def segundos(tiempo: str) -> int:
    hora, minutos, segundos = tiempo.split(":")
    hora = int(hora) * 3600
    minutos = int(minutos) * 60
    segundos = int(segundos) + hora + minutos
    return segundos


# B) La duración en horas, minutos y segundos de un intervalo dado en segundos.


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


resultado = segundos("01:23:36")
print(resultado)

resultado = intervalo(5016)
print(resultado)
