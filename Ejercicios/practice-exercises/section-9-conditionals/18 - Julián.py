"""
Crear un programa con un menú de una calculadora donde tendremos las 
opciones de suma, resta, multiplicación, división, resto (módulo) y salir. 
Introducimos dos números desde consola:
    1.- Suma.
    2.- Resta.
    3.- Multiplicación
    4.- División.
    5.- Resto
    6.- Salir
"""

while True:   

    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("-----------*CALCULADORA*--------------")
    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("1) Suma-------------------------------")
    print ("2) Resta------------------------------")
    print ("3) Multiplicación---------------------")
    print ("4) División---------------------------")
    print ("5) Resto------------------------------")
    print ("6) Salir------------------------------")
    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("--------------------------------------")
    print ("")
    print ("")
    print ("")

    variableElegida = int(input("Ingresá un número según qué operación quieras realizar: "))
   

    if variableElegida == 6:
        print("Nos vemos pronto wachín.")    
        break

    numeroUno = int(input("Ingresá valor del primer número: "))
    numeroDos = int(input("Ingresá valor del segundo número: "))

    if variableElegida == 1:
        print(f"El resultado de la suma es", numeroUno + numeroDos)

    elif variableElegida == 2:
        print(f"El resultado de la suma es", numeroUno - numeroDos)

    elif variableElegida == 3:
        print(f"El resultado de la suma es", numeroUno * numeroDos)

    elif variableElegida == 4:
        print(f"El resultado de la suma es", numeroUno / numeroDos)

    elif variableElegida == 5:
        print(f"El resultado de la suma es", numeroUno % numeroDos)

    else:
        print("Número no valido, ingresar otra opción.")



