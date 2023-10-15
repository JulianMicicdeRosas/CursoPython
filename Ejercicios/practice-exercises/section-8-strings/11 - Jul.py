"""
Escribe un programa en el que vamos a asignar a un string la siguiente frase 
“Estoy en la parte de la clase String 
del curso de ‘Bootcamp Python 3’ con el profesor Anartz Mugika. 
Luego aprenderé a trabajar con las estructuras de control del flujo de un 
programa :) Voy a escribir un correo electrónico a anartzmugika@anartz.com 
para preguntar una duda”.
Obtener los elementos en un array de tipo string separando los valores 
teniendo en cuenta los siguientes carácters (haciendo uso de la función replace):
“,”, “.”, “@”, “-” 
"""

Texto = ("Estoy en la parte de la clase String del curso de Bootcamp Python 3 con el profesor Anartz Mugika. \
         Luego aprenderé a trabajar con las estructuras de control del flujo de un programa :)\
        Voy a escribir un correo electrónico a anartzmugika@anartz.com para preguntar una duda")
          


Texto = Texto.replace(',', '_').replace('.', '_').replace('@', '_').replace('-', '_')

Texto_dividido = Texto.split('_')
print (len(Texto))

print (Texto_dividido)

