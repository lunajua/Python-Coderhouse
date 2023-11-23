'''Descripción de la actividad. 
Se tiene una cadena de texto, pero al revés. Al 
parecer contiene el nombre de un alumno, la nota 
de un examen y la materia. 
De forma individual, realiza lo siguiente: 
1. Dar vuelta la cadena y asignarla a una variable 
llamada cadena_volteada. Para devolver una 
cadena dada vuelta se usa el tercer índice 
negativo con slicing: cadena[::-1]. 
2. Extraer nombre y apellido, almacenarlo en una 
variable llamada nombre_alumno 
ACTIVIDAD EN CLASE
4. Extraer la nota y almacenarla en una variable 
llamada nota.
5. Extraer la materia y almacenarla en una variable 
llamada materia. 
6. Mostrar por pantalla la siguiente estructura: 
NOMBRE APELLIDO ha sacado un NOTA en
MATERIA'''

cadena = "acitametaM ,5.8 ,otipeP ordeP"

cadena_volteada = cadena[::-1]

print(cadena_volteada)

nombre_alumno = cadena_volteada[0:12]

print(nombre_alumno)

nota = float(cadena_volteada[14:17])

print(nota)

materia = cadena_volteada[19:]

print(materia)

print(nombre_alumno, "ha sacado un", nota, "en", materia)


