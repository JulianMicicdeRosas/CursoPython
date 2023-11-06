"""
Una tienda de videojuegos desea un programa para ingresar el valor de compra y 
calcular lo siguiente: si el pago se efectúa al “contado”, calcular un descuento 
del 10% pero si el pago es con “tarjeta” se incrementa un recargo del 2% al 
valor de compra. Calcular y visualizar el descuento o recargo según sea el caso 
y el total a pagar de la compra.
"""

MontoAPagar = 1000

print("============MONTO A PAGAR: $1000  ============")
print("============INGRESE MÉTODO DE PAGO============")
print("\t1) Contado")
print("\t2) Tarjeta")
print("\t3) Salir")
print("===================================")

MetodoDePago = int(input("Seleccione la opción deseada: "))


if (MetodoDePago == 1):
    resultado = MontoAPagar * 0.9
    print (f"El monto a pagar será con un descuento del 10%, por lo que le queda en {resultado}.")
elif (MetodoDePago == 2):
    resultado = MontoAPagar * 1.02
    print (f"El monto a pagar será con un recargo del 2%, por lo que le queda en {resultado}.")
else:
    print ("Usted ha salido del sistema. Usted debe correr.")