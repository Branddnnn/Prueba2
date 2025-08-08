"""
Se realizó un programa en el que se ingresan datos de una mascota como 
nombre, tipo, edad y sus vacunas, el mismo programa almacena los datos en un 
diccionario y los guarda en variables, verifica la edad, permite ingresar las 
vacunas que se le aplicaron y luego muestra un resumen de los datos.

Realizado por: Brandon Chan 01/05/2025
"""

mascota = {} #Diccionario de datos sobre una mascota

mascota["nombre"] = input("Ingrese el nombre de su mascota: ") #Primera variable del diccionario
mascota["tipo"] = input("Ingrese el tipo de mascota: ") #Segunda variable del diccionario

while True: #Tercera variable del diccionario, luego se verifíca la edad de la mascota
    edad = int(input("Ingrese la edad de su mascota: ")) 
    if 1 <= edad <= 10:
        mascota["edad"] = edad
        break
    print ("Edad no válida.")

vacunas = [] #Lista vacía para almacenar las vacunas aplicadas a la mascota

print("\nIngrese sus vacunas aplicadas (escribe 'fin' para terminar): ")
while True: #Permite ingresar las vacunas aplicadas que se quieran, para terminar se debe colocar la palabra 'fin'
    vacuna = input("Ingrese la vacuna aplicada: ")
    if vacuna.lower() == "fin":
        break
    if vacuna.lower() in [a.lower() for a in vacunas]:
        print(f"La vacuna '{vacunas}' ya está registrada.")
    else:
        vacunas.append(vacuna)
    
mascota["vacunas"] = vacunas #Cuarta variable del diccionario

print ("\nDatos de tu mascota:")#Resumen de datos sobre la mascota
print (f"Nombre : {mascota['nombre']}.")
print (f"Tipo   : {mascota['tipo']}.")
print (f"Edad   : {mascota['edad']} años.")
print ("Vacunas:")
for vacuna in mascota["vacunas"]:
    print (f" - {vacuna}")