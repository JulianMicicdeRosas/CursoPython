"""
Escribe un programa en en el que introducimos un número de 1 a 12 (incluidos) 
para hacer referencia al mes seleccionado. Una vez introducidos tenemos que 
devolver el número de días que tiene ese mes.
 Hay que tener en cuenta si el mes seleccionado es 2 (Febrero), deberíamos de 
 pedir el año para ver si ese año es bisiesto o no y con ello dar 29 días 
 (Bisiesto) o 28 días (No Bisiesto)

Meses con 31 días:
Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre
Meses con 30 días:
Abril, Junio, Septiembre, Noviembre
Febrero:
28 días si NO BISIESTO
29 días si BISIESTO
"""




num = int(input("introducir número entre 1 y 12, correspondiendo cada número a un mes del año: "))

if(num == 1):
    print("enero tiene 31 días")

elif(num == 2):
    año = int(input("introduzca el año para saber si es bisiesto, lo que variará el número de días de este mes: "))
    if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        print("febrero tiene 29 días")
    else:
        print("febrero tiene 28 días")

elif(num == 3):
    print("marzo tiene 31 días")

elif(num == 4):
    print("abril tiene 30 días")

elif(num == 5):
    print("mayo tiene 31 días")

elif(num == 6):
    print("junio tiene 30 días")

elif(num == 7):
    print("julio tiene 31 días")

elif(num == 8):
    print("agosto tiene 31 días")

elif(num == 9):
    print("septiembre tiene 30 días")

elif(num == 10):
    print("octubre tiene 31 días")

elif(num == 11):
    print("noviembre tiene 30 días")

elif(num == 12):
    print("diciembre tiene 31 días")





















"""
month = int(input("Introduzca el mes (1 y 12): \n"))

if (month >= 1 and month <= 12):  # mes válido
    if(month == 2):  # febrero => ¿Bisiesto?
        year = int(input("Introduzca el año: \n"))
        if ((year % 100 != 0 and year % 4 == 0) or year % 400 == 0):
            print("Este mes al ser febrero y BISIESTO tiene 29 días")
        else:
            print("Este mes al ser febrero y NO BISIESTO tiene 28 días")
    elif(month == 1 or month == 3 or month == 5 or month == 7
         or month == 8 or month == 10 or month == 12):
        print("Este mes tiene 31 días")
    else:
        print("Este mes tiene 30 días")
else:
    print("Debes de introducir un número entre 1 y 12 (incluido)")
"""