"""
Realizar un programa que imprima en pantalla los números del 100 al 1
(incluidos) que son múltiplos de 3.
Lo haremos con las diferentes opciones
* while
* for (usando “range”) y sin usar un condicional, solo con el uso del rango
"""




#while

i = 100

while i >= 1 and i <= 100: #NO HACE FALTA ESPECIFICAR QUE ES MENOR O IGUAL QUE 100 PORQUE NO VA A PARTIR DE UN NÚMERO MAYOR
    if i % 3 == 0:
        print (i)
        i = i - 1
    else:
        i = i - 1

                

#for
                
for i in range(100, 1, -1):
    if (i % 3 == 0):
        print (i)



























"""
# while
print("======================while (descontador - múltiplos de 3) ======================")
i = 100


Para obtener los múltiplos de 3 y para mostrarlos, ponemos la condición 
si la división de entre 3 es 0 en el resto. Con eso sabemos que es impar
y lo mostramos

while i >= 1:
    if ( i % 3 == 0): print(i)
    i -= 1

# for
print("======================for (descontador - múltiplos de 3) ======================")

En este caso aplicamos que por iteración haga + 2. Empezando de 1, que es
impar, si vamos sumando + tendremos 1, 3, 5, 7, 9, 11, 13, 15, 17, 
19, 21,...

for value in range(99, 0, -3):
    print(value)
"""