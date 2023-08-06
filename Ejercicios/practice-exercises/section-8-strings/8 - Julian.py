'''
Escribe un programa en el que vamos a asignar a un string la siguiente frase “Estoy haciendo los ejercicios opcionales del 
curso Bootcamp Python 3 con el profesor Anartz Mugika”. 
Vamos a realizar las siguientes comprobaciones y mostramos su resultado. Recordad que son diferentes los mismos 
carácteres que están en mayúsculas y minúsculas.
(Trabajar con startswith, igualdad ==, endswith)
Comienza con “Bootcamp Python 3”. => false
Comienza con “Estoy haciendo los ejercicios opcionales” => true
Es igual a “Estoy haciendo ejercicios opcionales” => false
Finaliza con “Mugika” => true
Finaliza con “AnartzMugika” => false
Finaliza con “Anartz Mugika” => true"
'''

StringLoca = "Estoy haciendo los ejercicios opcionales del curso Bootcamp Python 3 con el profesor Anartz Mugika"

ChequeandoComoComienza = StringLoca.startswith("Bootcamp Python 3")
print (ChequeandoComoComienza)

ChequeandoComoComienza2 = StringLoca.startswith("Estoy haciendo los ejercicios opcionales")
print (ChequeandoComoComienza2)

"""ChequeandoComoComienza2 = StringLoca.startswith("Estoy haciendo los ejercicios opcionales")
print ("El chequeo sobre si comienza con 'Estoy haciendo los ejercicios opcionales' sería: " (ChequeandoComoComienza2))"""""

ChequeandoIgualdad = StringLoca == "Estoy haciendo los ejercicios opcionales"
print ("El resultado sería " + str(ChequeandoIgualdad))

ChequeandoComoComienza = StringLoca.endswith("Mugika")
print (ChequeandoComoComienza)

ChequeandoComoComienza = StringLoca.endswith("AnartzMugika")
print (ChequeandoComoComienza)