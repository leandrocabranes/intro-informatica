def ordenamientoBurbujeoOptimizado(lista):
  desordenado = True
  for i in range(len(lista) - 1):
    desordenado = False
    for j in range(i+1, len(lista)):
      if lista[i] > lista[j]:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp

        desordenado = True

  return lista

print(ordenamientoBurbujeoOptimizado([1, 4, 7, 3, 26, 12,0, 2]))