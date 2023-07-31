"""
Escribe un programa que convierta el primer carácter en mayúsculas y 
los restantes 
en minúsculas de un string introducido por teclado.
No usar función 'capitalize'
"""

VariableParaIngresar = input("Ingresar palabrita para pasar a mayúscula la primer letra: ")
TextoConMayuscula = VariableParaIngresar[0].upper() + VariableParaIngresar[1:]

print(TextoConMayuscula) 
