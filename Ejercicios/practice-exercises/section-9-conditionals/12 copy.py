to_check = input("Escribir valor de: ")
to_check = int(to_check)

"""msg = ""

if to_check == 0:
    msg = "El valor es 0"
    print(msg)
elif to_check % 2 == 0 and to_check != 0:
    msg = "Par"
    print(msg)
else:
    msg = "Impar"
    print(msg)
"""

msg = ( "Cero" if to_check == 0 else "Par") 
if to_check % 2 == 0 else "Impar" 

print ("El número {} es {}".format(to_check, msg))