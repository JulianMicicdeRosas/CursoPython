"""
Escribe un programa donde vamos a introducir dos textos y vamos a comparar si son de la misma longitud y 
diferentes entre si.
Mostrar lo siguiente después de introducir los dos textos:
Resultado de lo introducido: <primerInput>,< segundoInput>
Longitud de <primerInput> es x carácteres.
Longitud de <segundoInput> es x carácteres.
¿Tienen la misma logitud? <respuesta_true_o_false>
¿Son iguales? (Comparar los dos valores>)

"""

Texto1 = input("\nIntroduzca el primer texto: ")
Texto2 = input("\nIntroduzca el segundo texto: ")

LongitudT1 = len(Texto1)
LongitudT2 = len(Texto2)

Concatenacion1 = f"Resultado de la introducido: <{Texto1}>, <{Texto2}>"
Concatenacion2 = "Longitud de <{}> es {} caracteres. \n Longitud de <{}> es {}".format(Texto1, LongitudT1, Texto2, LongitudT2)


print(Concatenacion1)

print(Concatenacion2)