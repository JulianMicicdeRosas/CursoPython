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

Temperatura = float(input("Insertar temperatura en grados centígrados: "))

#A partir de ahora vamos a chequear la temperatura y poner un print según valor

if Temperatura <= 0: 
    print ("Che, qué friazo, está *super frío*")
elif Temperatura > 0 and Temperatura < 10:
    print (f"Hacen {Temperatura}°, lo que significa que está muy frío")
elif Temperatura > 10 and Temperatura < 20:
    print (f"Hacen {Temperatura}°, lo que significa que está frío")
elif Temperatura > 20 and Temperatura < 30:
    print (f"Hacen {Temperatura}°, lo que significa que está normal")
elif Temperatura > 30 and Temperatura < 40:
    print (f"Hacen {Temperatura}°, lo que significa que está caluroso")
elif Temperatura <= 40:
    print (f"Hacen {Temperatura}°, lo que significa que está tropical")
else:
    print ("Ingresar temperatura nuevamente {0}".format(Temperatura))