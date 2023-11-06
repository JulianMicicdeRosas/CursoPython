"""
Vamos a crear un programa, donde introducimos un número ENTERO entre 0-999 y 
debemos de decir la cantidad de cifras que tiene. Si está fuera de ese rango 
debemos de avisar al usuario que está fuera del rango. 
No lo hagáis usando la clase str, con condicional if
Datos de prueba:
Introduce número: 18
Resultado esperado: El 18 tiene 2 cifras.

"""

PrimerNumero = int(input("Introduzca numerito entre 00 y 999: "))


if (PrimerNumero < 10 and PrimerNumero >= 10):
    print (f"El número {PrimerNumero} tiene 1 cifra")
elif (PrimerNumero < 100 and PrimerNumero >= 10):
    print (f"El número {PrimerNumero} tiene 2 cifras")
elif (PrimerNumero < 999 and PrimerNumero > 10):
    print (f"El número {PrimerNumero} tiene 3 cifras")
else:
    print ("Ese número no es lo pedido. Reingresar.")
