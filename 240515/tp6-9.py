"""
Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número entero N que representa una cantidad de días. Realizar un programa que imprima la nueva fecha que resulta de sumar N días a la fecha dada. Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3.
"""

def diasrestantes(dia, mes, anio):
  nuevoDia = 0
  nuevoMes = 0
  nuevoAnio = 0
  print(nuevoDia, nuevoMes, nuevoAnio)

def anioBisiesto(anio):
  if anio % 4 == 0 and anio % 100 != 0 and anio % 400 == 0:
    return True
  else:
    return False