"""
Una distribuidora de motocicletas tiene una promoción de fin de año que 
consiste en lo siguiente. Las motos marca Honda tienen un descuento del 5%, 
las marcas Yamaha del 8% y las Suzuki del 10%, las otras marcas 2%. 
Hay que pedir el nombre de la marca (se puede hacer con un menú inicial 
con las opciones para seleccionar) de la moto y también el precio de la moto.
"""

print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------*MARCAS*----------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("1) Yamaha-----------------------------")
print ("2) Suzuki-----------------------------")
print ("3) Honda------------------------------")
print ("4) Otra marca-------------------------")
print ("--------------------------------------")
print ("--------------------------------------")

marcaElegida = int(input("Ingrese marca de motocicleta a comprar: "))
montoAPagar = int(input("Ingrese el monto a pagar: "))
if marcaElegida == 1:
    print(f"Las motocicletas Yamaha tienen un descuento del 8%, por lo que deberás pagar ", montoAPagar*0.92)
elif marcaElegida == 2:
    print(f"Las motocicletas Suzuki tienen un descuento del 10%, por lo que deberás pagar ", montoAPagar*0.90)
elif marcaElegida == 3:
    print(f"Las motocicletas Suzuki tienen un descuento del 5%, por lo que deberás pagar ", montoAPagar*0.95)
elif marcaElegida == 4:
    print(f"Las motocicletas de otras marcas tienen un descuento del 2%, por lo que deberás pagar ", montoAPagar*0.98)
else:
    print("Has ingresado un valor inválido.")