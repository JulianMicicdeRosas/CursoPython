"""
La academia de Formación “Anartz Mugika Ledo Online” desea un programa para
ingresar por teclado el total de compra y el día de la semana si el día es
martes o jueves, se realizará un descuento del 15% por la compra. Si el día es
domingo, se descontará un 29% del total de la compra.
Visualizar el descuento y el total a pagar por la compra. Hay que tener en
cuenta que tienes que añadir un menú asociado para introducir un número entre
1-7 (incluidos) para hacer referencia a los días de la semana.
Hay que hacer una comprobación que introducimos un día de la semana correcta.
Si no está dentro del rango, NO SE APLICA DESCUENTO mostrando un mensaje
"El día de la semana es inexistente y no hay descuento para aplicar.
"""

martes= 2
jueves= 4
domingo= 7

print("CALCULADORA DE DESCUENTOS")
print("Anartz Mugika Ledo Online")
print("=========================")
precio= int(input("1) Ingresar valor de la compra: "))
datoIngresado= int(input("2) Ingresar número entre 1 y 7: "))


if ((datoIngresado < 1) or (datoIngresado > 7)):
    print("El día de la semana es inexistente y no hay descuento para aplicar.")
    #lo siguiente del código no es necesario para este ejercicio pero lo hice para probar
    print("A) Volver al Menú")
    print("B) Salir")
    ingresarAoB=int(input("Introduzca la opción deseada: ")) 
    #agregué "int" en la línea anterior pero venía funcionando bien sin eso
    
elif ((datoIngresado == 1) or (datoIngresado == 3) or (datoIngresado == 5) or (datoIngresado == 6)):
    print("El día de la semana no tiene descuento para aplicar.")

elif (datoIngresado == 2):
    print("Hoy es martes. Tiene un descuento del 15%")
    print("El Monto a pagar es: ",  float(precio - (precio*0.15)))

elif (datoIngresado == 4):
    print("Hoy es jueves. Tiene un descuento del 15%")
    print("El Monto a pagar es: ",  float(precio - (precio*0.15)))

elif (datoIngresado == 7):
    print("Hoy es domingo. Tiene un descuento del 29%")
    print("El Monto a pagar es: ",  float(precio - (precio*0.29)))
    



























"""


total = float(input("Introduce el importe total a pagar: "))
print("¿Qué día de la semana es?")
print("1) Lunes")
print("2) Martes")
print("3) Miércoles")
print("4) Jueves")
print("5) Viernes")
print("6) Sábado")
print("7) Domingo")
week_day = int(input("Introduce día de la semana: "))
print("=============================================")
print("Día introducido: {0}".format(week_day))
discount_value = 0
# Comprobar si estamos en el rango correcto del día seleccionado
if (week_day >= 1 and week_day <= 7):
    # Comprobar si es martes o jueves
    if (week_day == 2 or week_day == 4):  # 15% de descuento
        discount_value = total * 0.15
        print(f"Total a pagar (15% descuento) = {(total-discount_value):.3f}")
    elif(week_day == 7):
        discount_value = total * 0.29
        print(f"Total a pagar (29% descuento) = {(total-discount_value):.3f}")
    else:
        print(f"Total a pagar (sin descuento) = {total:.3f}", )
else:
    print("El día de la semana es inexistente y no hay descuento para aplicar")
    print(f"Total a pagar (sin descuento) = {total:.3f}")

    """