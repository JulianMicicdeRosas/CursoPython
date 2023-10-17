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


NumeroDeMes = int(input("Introduce un número del mes, del 1 al 12: "))

if NumeroDeMes == 2:
    NumeroDeAnio = int(input("Introduce en qué año estás: "))
    if NumeroDeAnio % 4 == 0 and NumeroDeAnio % 100 != 0 and NumeroDeAnio % 100 == 0 and NumeroDeAnio % 400 != 0: 
        print("Febrero tendrá 29 días.")
    else: 
        print("Febrero tendrá 28 días")
elif NumeroDeMes == 3:
    print("Has elegido el mes marzo")
elif NumeroDeMes == 4:
    print("Has elegido el mes abril")
elif NumeroDeMes == 5:
    print("Has elegido el mes mayo")
elif NumeroDeMes == 6:
    print("Has elegido el mes junio")
elif NumeroDeMes == 7:
    print("Has elegido el mes julio")
elif NumeroDeMes == 8:
    print("Has elegido el mes agosto")
elif NumeroDeMes == 9:
    print("Has elegido el mes septiembre")
elif NumeroDeMes == 10:
    print("Has elegido el mes octubre")
elif NumeroDeMes == 11:
    print("Has elegido el mes noviembre")
elif NumeroDeMes > 12 or NumeroDeMes % 1 !=0:
    print("No existe esa cantidad de meses en un año")
else:
    print("Flasheaste")



