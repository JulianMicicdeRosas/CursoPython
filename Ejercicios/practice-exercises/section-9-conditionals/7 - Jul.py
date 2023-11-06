"""
Convertidor Euros-Pesetas Españolas.
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



print("============CONVERTIDOR============")
print("\t1) Euros a Pesetas")
print("\t2) Pesetas a Euros")
print("\t3) Salir")
print("===================================")

Opcion = int(input("Introducir una opción: "))



if Opcion == 1:
    NumeroVariable = int(input("Introducir un número con el que trabajar "))
    Resultado = NumeroVariable * 166.386
    print ("La cantidad de pesetas total sería" + str(Resultado))
elif Opcion == 2:
    NumeroVariable = int(input("Introducir un número con el que trabajar "))
    Resultado = NumeroVariable / 166.386
    print ("La cantidad de pesetas total sería" + str(Resultado))
else: 
    print ("Listo, te mando un abrazo")

   