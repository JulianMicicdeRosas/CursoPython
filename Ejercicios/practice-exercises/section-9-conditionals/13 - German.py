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
montoTotal = 0

while True:
    print("================================")
    print("MENÚ:")
    print("A) Ingresar dinero a la cuenta: ")
    print("B) Retirar dinero de la cuenta: ") #(si queremos retirar más de lo que hay mostrar mensaje advirtiendo que no es posible 
    print("C) Salir")
    print("================================")

    letra = str(input())
    

    if(letra == "a" or letra == "A" ):
        montoTotal = float(montoTotal)
        ingreso = float(input("Por favor, ingrese el valor que desea añadir a su cuenta: "))  
        montoTotal += ingreso
        print("Dinero ingresado con éxito")
        print("El monto ha sido ingresado con éxito")
        print("Su saldo es de: ", montoTotal)
        

    elif(letra == "b" or letra == "B"):
        retiro = float(input("Por favor, ingrese el valor que desea retirar de su cuenta: "))
        if(retiro <= ingreso):
            montoTotal -= retiro
            print("El monto ha sido extraido con éxito")
            print("Su saldo es de: ", montoTotal)
            
            
        else:
            print("Se ha producido un error en la extracción. Intente nuevamente")

    elif(letra == "c" or letra == "C"):
                        print("Gracias por utilizar nuestros servicios")
                        break

    else:
           print("Opción no válida. Intente nuevamente")                    










"""
    elif(letra != "a" or letra != "A" or letra != "b" or letra != "B"):
                 if(letra != "c" or letra  != "C"):
                      print("Opción no válida. Intente nuevamente")
                 
                 elif(letra == "c" or letra == "C"):
                     print("Gracias por utilizar nuestros servicios")
                     break        
             
"""
    

        
        
















"""
total = 1000

# Comprobar si estamos en el rango correcto del día seleccionado
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta.")
print("3. Salir")

option = input("Selecciona operación: ")

if (option == "1"):
    add_money = float(input("¿Cuánto dinero quieres ingresar? "))
    total += add_money
    print("El saldo de tu cuenta después de añadir {0} euros es de {1} euros.".format(
        add_money, total
    ))
elif (option == "2"):
    quit_money = float(input("¿Cuánto dinero quieres retirar? "))
    if (quit_money > total): print("No puedes retirar {0} euros ya que tu saldo es de {1} euros".format(quit_money, total ))		 
    total -= quit_money
    print("El saldo de tu cuenta después de retirar {0} euros es de {1} euros.".format(
            quit_money, total
    ))
elif(option == "3"):
    print("Saliendo")
else: print("Opción incorrecta. Saliendo")
"""





















      
