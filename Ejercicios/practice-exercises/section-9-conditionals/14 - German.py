"""
Crear un programa que determine el mayor de 3 números DIFERENTES 
introducidos por teclado (float o int, podéis decidir).
Introduce primer número: 18
Introduce segundo número: -1
Introduce tercer número: 36
Resultado esperado: El número con valor mayor es 36.
"""




print("MAYOR NÚMERO")
numeroIngresado_1 = int(input("Ingrese el primer número: "))
numeroIngresado_2 = int(input("Ingrese el segundo número: "))
numeroIngresado_3 = int(input("Ingrese el tercer número: "))

if numeroIngresado_1 > numeroIngresado_2 and numeroIngresado_1 > numeroIngresado_3:
    print("El número mayor es: ", numeroIngresado_1)

elif numeroIngresado_2 > numeroIngresado_1 and numeroIngresado_2 > numeroIngresado_3:
    print("El número mayor es: ", numeroIngresado_2)

else:
    print("El número mayor es: ", numeroIngresado_3)











"""
number_one = int(input("Introduce primer número: "))
number_two = int(input("Introduce segundo número: "))
number_three = int(input("Introduce tercer número: "))

if (number_one == number_two or number_two == number_three
        or number_one == number_three):
    print("El requisito del programa exigía introducir números DIFERENTES")
elif(number_one > number_two and number_one > number_three):
    print(f"El primer valor es el mayor: {number_one}")
elif(number_one < number_two and number_two > number_three):
    print(f"El segundo valor es el mayor: {number_two}")
else:
    print(f"El tercer valor es el mayor: {number_three}")
"""


























