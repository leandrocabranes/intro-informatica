"""
Obtener el digito central si es par, sino devolver -1
Ejemplo: 12345 = 3 o 12 = -1
"""

def digitocentral(n):
  digito = 0
  posicion = 0
  cant_dig = cantidaddigitos(n)
  if cant_dig % 2 == 1:
    posicion = (cant_dig // 2) + 1
    segunda_mitad = n % 10 ** posicion
    digito = segunda_mitad // 10 ** (posicion -1)
    return digito
  else:
    return -1

def cantidaddigitos(n):
  contador_aux = True
  cant_digitos = 0
  while contador_aux:
    if n > 10 ** cant_digitos:
      cant_digitos = cant_digitos + 1
    else:
      contador_aux = False
  return cant_digitos

print(digitocentral(12343))
print(digitocentral(421))
print(digitocentral(4210))
print(digitocentral(42109000031))
print(digitocentral(434274210))
print(digitocentral(4213240))
print(digitocentral(8))