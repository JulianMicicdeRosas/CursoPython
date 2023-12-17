"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido en el lanzamiento de tres dados de un cliente, 
de acuerdo a los siguientes resultados:
Si los tres dados son seis => “Excelente”
Si dos dados dan seis => “Muy bien”
Si en un dado obtenemos seis => “Regular”
Si ninguno de los dados obtenemos seis => “Mal”
"""


print("Puntaje dados")
print("==================")

dado1 = int(input("Lance el primer dado: "))
dado2 = int(input("Lance el segundo dado: "))
dado3 = int(input("Lance el tercer dado: "))


if((dado1 >= 1 and dado1 <= 6) and (dado2 >= 1 and dado2 <= 6) and (dado3 >= 1 and dado3 <= 6)):

    if(dado1 != 6 and dado2 != 6 and dado3 != 6):
        print("Mal")
    elif((dado1 == 6 and dado2 != 6 and dado3 != 6) or (dado2 == 6 and dado1 != 6 and dado3 != 6) or (dado3 == 6 and dado2 != 6 and dado1 != 6)):
        print("Regular")
    elif((dado1 == 6 and dado2 == 6 and dado3 != 6) or (dado2 == 6 and dado1 == 6 and dado3 != 6) or (dado3 == 6 and dado2 == 6 and dado1 != 6)) :
        print("Muy bien")
    elif(dado1 == 6 and dado2 == 6 and dado3 ==6):
        print("Excelente")

else:
    print("Error inesperado. Por favor, reinicie el programa e intente nuevamente.")

#ver cómo está resuleto tal cuál venía 

"""
one = int(input("Introduce valor del primer dado: "))
two= int(input("Introduce valor del segundo dado: "))
three = int(input("Introduce valor del tercer dado: "))

if (1 > one or one > 6 or 1 > two or two > 6 or 1 > three or three > 6):
    print("El valor de alguno de los dados no es el correcto")

# Vamos a evaluar ya si es admitido o no el alumno
if ( one == 6 and two == 6 and three == 6):
    print("Excelente")
elif ( (one == 6 and two == 6) or (one == 6 and three == 6) or (three == 6 and two == 6)):
    print("Muy bien")
elif ( one == 6 or two == 6 or three == 6):
    print("Regular")
else:
    print("Mal")
"""