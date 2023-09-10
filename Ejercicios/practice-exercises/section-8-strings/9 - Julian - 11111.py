"""
Escribe un programa en el que vamos a asignar a un string la 
siguiente frase “Estoy haciendo los ejercicios opcionales del curso 
Bootcamp Python 3 con el profesor Anartz Mugika”.
Vamos a realizar las siguientes comprobaciones y mostramos su resultado. 
Recordad que son diferentes los mismos carácteres que están en mayúsculas y 
minúsculas.
(Trabajar con index, selección por rangos)
Extraer “Bootcamp Python 3” teniendo en cuenta que coge el nuevo string 
creado haciendou so de la función index buscando “Bootcamp”. Al obtener 
la posición, tener en cuenta 
la longitud de "Bootcamp Python 3" para extraerlo.
"""

Texto = "Estoy haciendo los ejercicios opcionales del curso Bootcamp Python 3 con el profesor Anartz Mugika"

Posicion_inicial = Texto.index("Bootcamp P")
Extension_for_extraction = len("Bootcamp Python 3")

Extract_word = Texto[Posicion_inicial : Posicion_inicial + Extension_for_extraction]

print (Extract_word)