"""
Vamos a crear un programa, donde introducimos un número ENTERO y 
debemos de decir si es PAR o IMPAR.
Datos de prueba:
Introduce el número: 5
Resultado esperado: 5 es IMPAR.

Introduce el número: 6
Resultado esperado: 6 es PAR.

"""

numero_uno = int(input("Introducir un número: "))

if (numero_uno % 2 == 0):
    paraImprimir = "El número {} es par".format(numero_uno)
    print(paraImprimir)
    
    """(numero_uno, "es par")"""
else:
    paraImprimir = "El número {} es impar".format(numero_uno)
    print(paraImprimir)
    
    
    """(numero_uno, "no lo es")"""
