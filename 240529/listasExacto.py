"""
Realizar un programa que ingese n nombres, luego imprime los nombres
"""

ncorrecto = False
n = 0
nombres = []
while not ncorrecto:
  n = int(input("Ingrese N mayor o igual a 1, para determinar la cantidad de nombres a ingresar: "))
  if n < 1:
    print("Ingrese un numbero mayor o igual a 1")
  else:
    ncorrecto = True

for i in range(0, n):
  nombre = input("Ingrese nombre #{0}: ".format(str(i + 1)))
  nombres.append(nombre)

for i in range(0, n):
  print(nombres[i])
