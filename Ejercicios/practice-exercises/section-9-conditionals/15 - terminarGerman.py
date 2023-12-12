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


print("PROGRAMA DE ADMISIÓN")
cSharp = int(input("Introduce nota de C#: "))
unity = int(input("Introduce nota de Unity: "))
windowsForms = int(input("Introduce nota de Windows Forms: "))


if((cSharp <= 100 and cSharp >= 0) and (unity <= 100 and unity >= 0) and (windowsForms <= 100 and windowsForms >= 0)):  
         
    if(((cSharp >= 65 and cSharp <= 100 and cSharp >= 0) or (unity >= 55 and unity <= 100 and unity >= 0)\
     and (windowsForms >= 50 and windowsForms <= 100 and windowsForms >= 0)) or (cSharp + unity >= 160 and windowsForms >= 35)\
     or (cSharp + windowsForms + unity >= 180)): 
   
         print("ADMITIDO: SÍ")
    else:
         print("ADMITIDO: NO")

else:    
    print("Añadir las notas de 0 a 100, por favor")

   
    



"""
elif((cSharp < 0 or cSharp > 100) or (windowsForms < 0 or windowsForms> 100) or (unity < 0 or unity > 100)):


 else:
        print("ADMITIDO: NO")

elif( cSharp < 0 or unity < 0 or windowsForms < 0 or \
        cSharp > 100 or unity > 100 or windowsForms > 100):
    print("Añadir las notas de 0 a 100 por favor")
"""

















"""
c_sharp = float(input("Introduce la nota de C# (de 0 a 100): "))
unity = float(input("Introduce la nota de Unity (de 0 a 100): "))
windows_forms = float(
    input("Introduce la nota de Windows Forms (de 0 a 100): "))

if (0 > c_sharp or c_sharp > 100 or 0 > unity or unity > 100 or 0 > windows_forms or windows_forms > 100):
    print("Añadir las notas de 0 a 100 por favor")

# Vamos a evaluar ya si es admitido o no el alumno
if (c_sharp >= 65 and unity >= 55 and windows_forms >= 50 or
        (c_sharp + unity) >= 160 and windows_forms >= 35 or
        (c_sharp + unity+windows_forms) >= 180):
    print("ADMITIDO: SI")
else:
    print("ADMITIDO: NO")
"""

