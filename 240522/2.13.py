def binarioDecimal(binario=1):
  contador = 0
  decimal = 0
  base = 2
  while binario != 0:
    binarioTemp = binario / 10
    resto = binarioTemp % 1
    if resto != 0:
      decimal = decimal + (base ** contador)
      binario = binarioTemp - 0.1
    else:
      binario = binarioTemp

    contador = contador + 1

  return decimal

binario1 = input("Ingrese un numero binario: ")

print("El resultado de convertir " + str(binario1) + " a decimal es " + str(binarioDecimal(int(binario1))))
