"""
realizar un progrmaa que ingrese nombres hasta nombre sea igual a xx, luego se pide imprimir nombres
"""

nombre = ""
nombres = []

print("Para cortar la ejecución del programa ingrese xx como nombre")

while nombre != "xx":
  nombre = input("Ingrese un nombre: ")
  if nombre != "xx":
    nombres.append(nombre)

for i in range(0, len(nombres)):
  print(nombres[i])