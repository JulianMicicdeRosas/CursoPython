"""
Escribe un programa en el que vamos a asignar a un string la siguiente 
frase “Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’
con el profesor Anartz Mugika. Luego aprenderé a trabajar con las 
estructuras de control del flujo de un programa :)”. 

Vamos a extraer con split separando con el carácter “.” y asignaremos dentro de un list y evaluamos su longitud que debe de 
ser 2 
(la longitud se evalua como un str). Acceder a las posiciones index 0 y 1 también.
(Trabajar con split)

"""

Texto_completo = ("Estoy en la parte de la clase String del curso de ‘Bootcamp Python 3’ con el profesor Anartz Mugika. \
Luego aprenderé a trabajar con las estructuras de control del flujo de un programa :)") 

Resultado_del_split = Texto_completo.split(".")

print ("El resultado de la división nos da {} listados dentro de una nueva variable".format(len(Resultado_del_split)))
print ("Dentro de ese nuevo listado, si buscamos el contenido del index 0, daría {}  ".format(Resultado_del_split[0]))
print ("Dentro de ese nuevo listado, si buscamos el contenido del index 1, daría {}  ".format(Resultado_del_split[1]))

#print (Resultado_del_split[0])
#print (Resultado_del_split[1])