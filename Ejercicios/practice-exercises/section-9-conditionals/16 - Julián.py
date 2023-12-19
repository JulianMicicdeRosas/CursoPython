"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido en el 
lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis => “Excelente”
Si dos dados dan seis => “Muy bien”
Si en un dado obtenemos seis => “Regular”
Si ninguno de los dados obtenemos seis => “Mal”
"""

dadoUno = int(input("Ingrese valor de dado uno: "))
dadoDos = int(input("Ingrese valor de dado dos: "))
dadoTres = int(input("Ingrese valor de dado tres: "))
valorPosible = 6

if (dadoUno == dadoDos == dadoTres == valorPosible):
    print ("Excelente")

elif ((dadoUno != valorPosible) and (dadoDos == dadoTres == valorPosible)) or ((dadoDos != valorPosible) and (dadoUno == dadoTres == valorPosible)) or ((dadoTres != valorPosible) and (dadoDos == dadoUno == valorPosible)):
    print ("Muy bien")

elif (dadoUno == valorPosible or dadoDos == valorPosible or dadoTres == valorPosible):
    print ("Regular")

elif ((dadoUno == dadoDos == dadoTres) != valorPosible):
    print ("Mal")