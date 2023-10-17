"""
Vamos a crear un programa, donde introducimos un número ENTERO y 
debemos de decir si es POSITIVO, NEGATIVO ó NEUTRO (igual a 0).
Datos de prueba:
Introduce el número: -373
Resultado esperado: -373 es NEGATIVO

Introduce el número: 6
Resultado esperado: 6 es POSITIVO.


"""

numero = input("Introducir un número entero por favor: ")
numero = int(numero)

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es neutro")
else:
     print("El número es negativo") 