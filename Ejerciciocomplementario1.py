'''Consigna

Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales,
cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:  
Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
nota_1 cuenta como el 20% de la nota final
nota_2 cuenta como el 30% de la nota final
nota_3 cuenta como el 50% de la nota final'''

#Pido al alumno que ingrese las notas del primer examen, segundo examen y tercer examen.

nombre_alumno = input("Ingrese el nombre del alumno: ")

examen_1 = float(input(f"Ingrese la nota del primer examen del alumno {nombre_alumno}: "))

examen_2 = float(input(f"Ingrese la nota del segundo examen del alumno {nombre_alumno}: "))

examen_3 = float(input(f"Ingrese la nota del tercer examen del alumno {nombre_alumno}: "))

#Realizamos el calculo de la nota final, teniendo en cuenta los porcentajes asociados a cada nota

nota_final = (examen_1 * 0.2) + (examen_2 * 0.3) + (examen_3 * 0.5)

#Mostramos por pantalla la nota final del alumno

print(f"La nota final del alumno {nombre_alumno} es: {nota_final}")

