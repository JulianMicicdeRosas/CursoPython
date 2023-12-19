"""
Un obrero necesita calcular su salario semanal, el cual se obtiene de la 
siguiente manera:
Si trabaja 40 horas o menos se le paga 16 euros por hora
Si trabaja mas de 40 horas se le paga 16 euros por cada una de 
las primeras 40 horas y 20 euros por cada hora extra.
"""


print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
print ("¦¦¦¦*CALCULADORA DE SALARIO*¦¦¦¦¦¦¦")
print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")

cantidadDeHoras = int(input("Ingresá el número de horas que trabajás: "))
if cantidadDeHoras <= 40: 
    print("Vas a cobrar", 16*cantidadDeHoras)
elif cantidadDeHoras > 40:
    print("Vas a cobrar", (40*16) + (cantidadDeHoras - 40)*20)