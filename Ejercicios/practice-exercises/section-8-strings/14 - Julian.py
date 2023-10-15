"""
Siguiendo el ejercicio anterior, vamos a añadirle un apartado donde 
nos muestra un mensaje “Seleccione la opción deseada” 
(sin NINGÚN SALTO DE LÍNEA) y leer mediante teclado lo que introducimos.
Preguntamos mediante el operador relacional: ¿Está entre 1 y 4 (incluidos)?
¿Es igual a 5?
"""
print("===========================================================")
print("\t\tAHORCADO - OPCIONES DEL JUEGO")
print("===========================================================")
print("1) Jugar a acertar una palabra aleatoria.")
print("2) Jugar a acertar cinco palabras aleatorias.")
print("3) Jugar a acertar una palabra de un tema seleccionado")
print("4) Jugar a acertar cincos palabras de un tema seleccionado")
print("5) Salir.")
print("===========================================================")

print ("Seleccione la opción deseada")
opcion_elegida = int(input("Ingresar un número del 1 al 5: "))
print ("¿Está el número entre 1 y 4?")

if 1 <= opcion_elegida <= 4:
    print("El número 1 está entre 1 y 4 (inclusive).")
else:
    print("Has salido del programa. Espero que tengas un lindo día")