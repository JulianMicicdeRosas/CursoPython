"""
Diseñe un programa que lea la temperatura en centígrados del día e imprima el 
tipo de clima de teniendo como referencia la siguiente tabla:
Temperatura den Cº (TP)
Tipo de clima
Menor ó igual que 0
Super Frío
Mayor que 0 y menor ó igual que 10
Muy frio
Mayor que 10 y menor ó igual que 20
Frio
Mayor que 20 y menor ó igual que 30
Normal
Mayor que 30 y menor ó igual que 40
Caluroso
Mayor que 40
Tropical
"""



print("ESTADO DEL TIEMPO")
temp=float(input("La temperatura del día es de: "))

if(temp <= 0):
    print("La temperatura del día es de {}°. El clima es super frío".format(temp))

elif(temp > 0 and temp <= 10):
    print("La temperatura del día es de {}°. El clima es muy frío".format(temp))

elif(temp >10 and temp <= 20):
    print("La temperatura del día es de {}°. El clima es frío".format(temp))

elif(temp >20 and temp <= 30):
    print("La temperatura del día es de {}°. El clima es normal".format(temp))

elif(temp <30 and temp <= 40):
    print("La temperatura del día es de {}°. El clima es caluroso".format(temp))

else:
    print("La temperatura del día es de {}°. El clima es tropical".format(temp))

















"""
total = float(input("Introduce la temperatura en Cº: "))
		
# Comprobar si estamos en el rango correcto del día seleccionado
if (total <= 0):
    print("{0}ºC => Clima Super Frío".format(total))
elif(total >= 0 and total <= 10):
    print("{0}ºC => Clima Muy Frío".format(total))
elif(total >= 10 and total <= 20):
    print("{0}ºC => Clima Frío".format(total))
elif(total >= 20 and total <= 30):
    print("{0}ºC => Clima Normal".format(total))
elif(total >= 30 and total <= 40):
    print("{0}ºC => Clima Caluroso".format(total))
else:
    print("{0}ºC => Clima Tropical".format(total))
    """