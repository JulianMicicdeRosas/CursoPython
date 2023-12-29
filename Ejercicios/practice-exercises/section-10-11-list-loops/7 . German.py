"""
Basándonos en lo que hemos aprendido antes, vamos a añadir algunos 
casos como los siguientes.
1) Imprimir los números del 1 al 75 (incluido).
2) Imprimir los números del 50 al 100 (incluido).
3) Imprimir los números del -50 al 0 (incluido).
Especificamos el valor inicial y final. Si el inicial es menor que el final, 
cuenta de manera ascendente y si no, de manera descendente. No hay rango de 
números a introducir, vamos a procurar que entre el menor y el final no haya 
una diferencia mayor de 100 números.
"""

# Apartado para introducir el valor inicial y el de final
# Tienen que cumplir varios requisitos
# Entre el valor inicial y el final, máximo 100 de diferencia

#1)
i = 1

while i >= 1 and i <= 100:
        
        if(i <= 75):
        
            print (i)
            i += 1
        else:
            i += 1

#2)
i = 50

while i >= 50 and i <= 100:
     
     print (i)
     i += 1


#3)
i = -50

while i >= -50 and i <= 0:
     
     print (i)
     i += 1




"=============================================================="

input_values_correct = False
while (input_values_correct == False):
    start_value = int(input("Introduce el valor inicial " +
                            "(puede ser negativo): "))
    finish_value = int(input("Introduce el valor final " +
                             "(puede ser negativo): "))
    if start_value <= finish_value:
        difference = finish_value - start_value
    else:
        difference = start_value - finish_value

    if (difference <= 100):
        input_values_correct = True
    else:
        print("Diferencia entre los números introducidos es mayor a 100")

print("Final")

# Si inicio mayor que el final => descendendete
# Si no cumple lo anterior, ascendente
if (start_value >= finish_value):
    list = range(finish_value, start_value + 1, -1)
else:
    list = range(start_value, finish_value + 1, 1)

# Imprimir la información
for value in list:
    print(value)

