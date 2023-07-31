"""
Escribe un programa que concatene en una variable con la función format 
los tres textos que vamos a introducir desde el teclado en la consola, 
tiene que estar separados por un tabulador entre palabras y finalmente 
imprimimos el resultado de la variable nueva. 
Procurad tener en cuenta el salto de línea para el texto que se introduce.
"""

Variable_1 = input ("Introduce el valor de la variable 1: \n ")
Variable_2 = input ("Introduce el valor de la variable 2: \n ")
Variable_3 = input ("Introduce el valor de la variable 3: \n ")

Variable_final = Variable_1 + "\t" + Variable_2 + "\t" + Variable_3

print (Variable_final)
print(f"El resultado del print concatenado sería: {Variable_1} \t + {Variable_2} \t + {Variable_3}")