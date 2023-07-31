"""
Escribe un programa que concatene en dos variables, por un lado con la 
función “format” y por otro con “f-string” una lista de 5 productos 
que se mostrarán solo CON UN print y su contenido, elemento a elemento 
tendrán un salto de línea (mirar bien los carácteres de escape).
"""

Variable1 = input("Producto 1: ")
Variable2 = input("Producto 2: ")
Variable3 = input("Producto 3: ")
Variable4 = input("Producto 4: ")
Variable5 = input("Producto 5: ")

Concatenamiento1 = "Hola, bienvenides a Carrefour. Tenemos {}, {}, {}, {} y {}".format(Variable1, Variable2, Variable3, Variable4, Variable5)
Concatenamiento2 = f"Hola, bienvenides a Carrefour. Tenemos {Variable1}, {Variable2}, {Variable3}, {Variable4} y {Variable5}"

print(Concatenamiento1)
print(Concatenamiento2)