"""
Realizar un programa que imprima en pantalla los números impares del 100 al 1 (incluidos).
Lo haremos con las diferentes opciones
* while
* for (usando “range”) y sin usar un condicional, solo con el uso del rango
"""

# while

i = 100

while (i >= 1 and i <= 100):
    if (i % 2 != 0):
        print (i)
    
    i = i - 1
#línea 17 también se puede escribir: i -= 1




#for
    
i = 100

for i in range (99, 0, -2):
    print (i)














