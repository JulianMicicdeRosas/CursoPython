"""
Una distribuidora de motocicletas tiene una promoción de fin de año que 
consiste en lo siguiente. Las motos marca Honda tienen un descuento del 5%, 
las marcas Yamaha del 8% y las Suzuki del 10%, las otras marcas 2%. 
Hay que pedir el nombre de la marca (se puede hacer con un menú inicial 
con las opciones para seleccionar) de la moto y también el precio de la moto.
"""

print("===========================")
print("Seleccione marca de la moto")
print("===========================")
print("1) Honda...............5%")
print("2) Yamaha..............8%")
print("3) Suzuki.............10%")
print("4) Otras...............2%")

moto = int(input())
valorMotoFinal = 456

if(moto == 1):
    print("Ha elegido la marca Honda.")
    valorMoto = int(input("Ingrese el valor de la moto: "))
    descuento = 0.05
    print("El monto a pagar es: $", valorMoto-descuento*valorMoto)




#YA TENIENDO EL PRECIO DE LAS MOTOS EN LISTA:
"""
if(moto == 1):
    print("Ha elegido la marca Honda. El precio de la moto es de $7623. Con el descuento aplicado, usted deberá pagar $",7623-(7623*0.05))
if(moto == 2):
    print("Ha elegido la marca Yamaha. El precio de la moto es de $8000. Con el descuento aplicado, usted deberá pagar $",8000-(8000*0.08))
if(moto == 3):
    print("Ha elegido la marca Suzuki. El precio de la moto es de $5314. Con el descuento aplicado, usted deberá pagar $",5314-(5314*0.10))
if(moto == 4):
    print("Ha elegido 'Otras marcas'. El precio de la moto es de $2374. Con el descuento aplicado, usted deberá pagar $",2374-(2374*0.02))
"""



























"""
print("============MOTOS============")
print("1) Honda")
print("2) Yamaha")
print("3) Suzuki")
print("4) Otra marca")
print("========================")

option = input("Seleccione la marca:\n")
if (option == "1" or option == "2" or option == "3" or option == "4"):
    price = float(input("Precio a pagar:\n"))
    if (option == "1"):
        print(f"Honda (Descuento %5) = {price - (price * 0.05)}" )
    elif (option == "2"): 
        print(f"Yamaha (Descuento %8) = {price - (price * 0.08)}" )
    elif (option == "3"): 
        print(f"Suzuki (Descuento %10) = {price - (price * 0.1)}" )
    elif (option == "4"): 
        print(f"Otras (Descuento %2) = {price - (price * 0.02)}" )
else:
    print("Opción incorrecta")
"""
