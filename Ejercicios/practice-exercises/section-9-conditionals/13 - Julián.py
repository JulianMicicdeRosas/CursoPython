"""
Hacer un programa haciendo uso del switch que simule un cajero automático
con un saldo inicial de 1000 euros, con el siguiente menú de opciones:
MENÚ:
* Ingresar dinero a la cuenta
* Retirar dinero de la cuenta (si queremos retirar más de lo que hay,
mostrar mensaje advirtiendo que no es posible)
* Salir
(Si no seleccionamos correctamente ni 1,2 ni 3, para decir “Opción incorrecta)

"""

dineroInicial = 1000

print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("----------------*MENÚ*----------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("1) Ingresar dinero a la cuenta--------")
print ("2) Retirar dinero de la cuenta--------")
print ("3) Salir------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("")
print ("")
print ("")

opcion = input("Elige una opción: ")

if opcion == "1":
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦*INGRESAR DINERO*¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("")
    print ("")
    print ("")

    montoIngresado = float(input("Digita el dinero a ingresar: "))
    print ("")
    print ("")
    print ("")
    print (f"Tu dinero total es de ${dineroInicial + montoIngresado}")

elif opcion == "2":
    montoIngresado = float(input("Digita el dinero a retirar: "))
    print ("")
    print ("")
    print ("")
    print (f"Tu dinero total es de ${dineroInicial - montoIngresado}")

else:

    print (f"Has terminado las operaciones. Que tengas un buen día")
