"""
Crear un programa que determine el mayor de 3 números DIFERENTES 
introducidos por teclado (float o int, podéis decidir).
Introduce primer número: 18
Introduce segundo número: -1
Introduce tercer número: 36
Resultado esperado: El número con valor mayor es 36.
"""
bucle = 0 

while bucle == 0: 

    print ("")
    print ("")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦*INTRODUCE EL PRIMER VALOR*¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("")
    print ("")

    numeroUno = int(input("Introduce valor del primer valor: "))

    print ("")
    print ("")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦*INTRODUCE EL SEGUNDO VALOR*¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("")
    print ("")


    numeroDos = int(input("Introduce valor del segundo valor: "))

    print ("")
    print ("")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦*INTRODUCE EL TERCER VALOR*¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
    print ("")
    print ("")


    numeroTres = int(input("Introduce valor del tercer valor: "))

    print ("")
    print ("")

    if numeroUno == numeroDos or numeroUno == numeroTres or numeroTres == numeroDos:
        print ("")
        print ("")
        print ("Reingresar al programa: los números deben tener valores diferentes.")
        print ("")
        print ("")

    elif numeroDos < numeroUno > numeroTres:
        print ("")
        print ("")
        print (f"El el primer valor, el número {numeroUno} es el de mayor valor.")
        print ("")
        print ("")

    elif numeroUno < numeroDos > numeroTres:
        print ("")
        print ("")
        print (f"El segundo valor, el número {numeroDos} es el de mayor valor.")
        print ("")
        print ("")  

    else:
        print ("")
        print ("")
        print (f"El tercer valor, el número {numeroTres} es el de mayor valor.")
        print ("")
        print ("")
