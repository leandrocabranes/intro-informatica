def busquedaBinaria(lista, valor):
  ls = len(lista) - 1
  li = 0

  while li <= ls:
    medio = (li + ls) // 2

    if lista[medio] == valor:
      return medio

    if lista[medio] < valor:
      li = medio + 1
    else:
      ls = medio - 1
  return -1

print(busquedaBinaria([1, 3, 6, 8, 10, 15, 17, 20], 17))