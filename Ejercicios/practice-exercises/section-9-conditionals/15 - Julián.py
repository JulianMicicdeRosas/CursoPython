"""
Escriba un programa para determinar la elegibilidad de admisión para un 
curso profesional según los siguientes criterios
Introduce nota de C#: (de 0 a 100)
Introduce nota de Unity: (de 0 a 100)
Introduce nota de Windows Forms: (de 0 a 100)
ADMITIDO: SI (o NO)
(Si alguna nota no entra en el rango, mostrar un mensaje "Añadir las 
notas de 0 a 100 por favor" y no evaluarlo")
        
Debe de cumplir uno de estos criterios
C# >= 65
Unity >= 55
Windows Forms >= 50
ó
Suma de C# y Unity >= 160
Windows Forms >= 35
ó
Total en las 3 materias>= 180.
"""

print ("")
print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
print ("¦¦¦¦¦*ADMISIÓN AL CURSO LOCO*¦¦¦¦¦¦")
print ("¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦")
print ("")

notaC = int(input("Introduce valor del 0 al 100 del puntaje en números de C#: "))
notaUnity = int(input("Introduce valor del 0 al 100 del puntaje en números de Unity: "))
notaWindows = int(input("Introduce valor del 0 al 100 del puntaje en números de Windows Forms: "))

if 0 > notaC < 100:
    print ("Ingresar un valor entre 0 y 100 por favor.")
    
if 0 > notaWindows < 100:
    print ("Ingresar un valor entre 0 y 100 por favor.")

if 0 > notaUnity < 100:
    print ("Ingresar un valor entre 0 y 100 por favor.")


if (notaC >= 65 or notaUnity >= 55 or notaWindows >= 50) or (((notaC + notaUnity) >= 160 and notaWindows >= 35)) or ((notaC + notaUnity + notaWindows) == 180):
    print ("¡Has ingresado al Curso Loco!")

else:
    print ("Lo lamento, no has ingresado al Curso Loco.")
