"""
Vamos a crear un programa, donde introducimos un año cualquiera (número ENTERO)
y comprobamos si es bisiesto o no el año.
Tenemos que tener en cuenta lo siguiente, para saber si es un año bisiesto o no:

Hay que tener estas condiciones, con que cumpla una de ellas es suficiente:
No divisible de 100 y divisible de 4. Si cumple Bisiesto. Si no, No bisiesto
Divisible de 400. Si cumple => Bisiesto. Si no cumple seguir al siguiente paso.
Datos de prueba:
Introduce un año: 2016
Resultado esperado: 2016 es BISIESTO.
Introduce el número: 2017
Resultado esperado: 2017 NO es BISIESTO.
Pista, mediante operadores lógicos podemos hacer la pregunta para saber si es
bisiesto o no, tener en en cuenta el uso de paréntesis, AND, OR,...
Los años bisiestos entre 1582 y 2200: 
https://miniwebtool.com/es/leap-years-list/?end_year=2200&start_year=1582

"""
ChequearNumero = int(input("Introducir un número para ver si es bisiesto: "))

if ChequearNumero % 4 == 0 and ChequearNumero % 100 != 0 and ChequearNumero % 100 == 0 and ChequearNumero % 400 != 0: 
    print("Es un año bisiesto.")
else: 
    print ("No es un año bisiesto")



