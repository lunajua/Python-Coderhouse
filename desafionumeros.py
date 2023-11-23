# En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo. Para ello, debemos considerar tres aspectos:

# jugaron 20 partidos durante el torneo,
# los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos,
# el promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

partidos_jugados = 20

puntaje_ganados = 3

puntaje_empatados = 1

puntaje_perdidos = 0

ganados = int(input("¿Que cantidad de partidos gano tu equipo?:\n "))

perdidos = int(input("¿Que cantidad de partidos perdio tu equipo?:\n "))

empatados = int(input("¿Que cantidad de partidos empatado tu equipo?:\n "))

puntaje = puntaje_ganados * ganados + puntaje_empatados * empatados + puntaje_perdidos * perdidos

print(f"El puntaje total fue de: {puntaje}")

puntaje_total = puntaje / partidos_jugados

print(f"El promedio final fue de: {puntaje_total} puntos")  