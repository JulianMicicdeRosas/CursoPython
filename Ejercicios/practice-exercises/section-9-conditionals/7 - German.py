"""
Convertidor Euros-Pesetas Españolas.n
Vamos a crear un programa, donde tenemos un menu inicial con varias opciones que usaremos para seleccionar la que deseamos ejecutar en todo momento.
1 - Convertir una cantidad de euros introducida en pesetas
2 - Convertir una cantidad de pesetas en euros.
3 - Salir.
Si no introducimos correctamente 1,2 mostrar un mensaje “Opción incorrecta. Prueba de nuevo por favor”
Sabiendo que  1 euro = 166,386 pesetas españolas.
Ejemplo:
Euros-> Pesetas = 16 euros son 2.662,176 pesetas españolas
Pesetas->Euros=100000 pesetas españolas son 601,0121euros

"""



print("\n - - - - - - MENÚ - - - - - - -\n\n ------------------------------ \n")
numero = int(input("1 - Convertir una cantidad de euros introducida en pesetas\n2 - Convertir una cantidad de pesetas en euro \n3 - Salir"))


if(numero == 1):
    eurosIngresados = int(input("introduzca cantidad de euros: "))
    resultado = eurosIngresados * 3465
    print("La cantidad de pesetas ingresada es igual a" + str(resultado))

elif(numero == 2):
    pesetasIngresadas=  int(print("introduzca cantidad de pesetas: " ))
    print(str("La cantidad de euros ingresada es igual a" + pesetasIngresadas * 2 ))

elif(numero == 3):
    (print("El programa ha finalizado con éxito"))

elif(numero != 1 or numero != 2 or numero != 3):
    print("Respuesta incorrecta. Intente nuevamente")


 















"""


print("============CONVERTIDOR============")
print("\t1) Euros a Pesetas")
print("\t2) Pesetas a Euros")
print("===================================")

option = input("Tipo de conversión a realizar: ")
if (option == "1" or option == "2"):
    value = float(input("Cantidad a convertir: "))
    if (option == "1"):	
        print("{0} €uros en Pesetas son: {1}".format(value, value * 166.386))
    elif(option == "2"):
        print("{0} Pesetas en €uros es: {1}".format(value, value / 166.386))
else:
    print("Opción incorrecta")

    """