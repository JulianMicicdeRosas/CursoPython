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

frase = ("Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’ con el profesor Anartz Mugika.\
Luego aprenderé a trabajar con las estructuras de control del flujo de unprograma :)\
Voy a escribir un correo electrónico a anartzmugika@anartz.com para preguntar una duda")


frase = frase.replace(',', '_').replace('.', '_').replace('@', '_').replace('-', '_')

#print (frase)

fraseDividida = frase.split('_')

print ("primera frase: ", fraseDividida[0])
print ("segunda frase: ", fraseDividida[1])
print ("tercera frase: ", fraseDividida[2])
print ("cuarta frase: ", fraseDividida[3])

