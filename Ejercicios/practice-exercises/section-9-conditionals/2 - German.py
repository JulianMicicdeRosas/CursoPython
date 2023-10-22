"""
Vamos a crear un programa, donde introducimos un número ENTERO y 
debemos de decir si es PAR o IMPAR.
Datos de prueba:
Introduce el número: 5
Resultado esperado: 5 es IMPAR.

Introduce el número: 6
Resultado esperado: 6 es PAR.

"""




"""
holis=int(input("introducir un número entero: {}".format(numero)))

if(holis % 2 == 0):
    print(numero, "es par")
else:
    print(numero, "es impar")
"""



numero = int(input("Introducir un número entero: "))

mensaje = "El número {} es".format(numero)

if numero % 2 == 0:
    mensaje += " par."
else:
    mensaje += " impar."

print(mensaje)






"""

number_val = int(input("Introduce el número: \n"))


if (number_val % 2 == 0): result = "PAR"
else: result = "IMPAR"

print(f"{number_val} es {result}")


"""