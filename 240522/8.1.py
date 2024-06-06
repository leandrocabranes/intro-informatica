"""
estructura legajo:
Legajo | Nota
-------------
      1|    4
      2|    2
      3|    8
      4|    5
      5|    2
"""

# lista = [4,12,5,5,7,3,3,5,7]
# listaOrdenada = []

# cont = 0

# while cont < len(lista):
#   for i in range(0, len(lista)):



legajos = [
  [1, 4],
  [5, 2],
  [10, 9],
  [3, 4]
]

print(legajos)

def ordenarLista(listaLegajos):
  for i in range(0, len(listaLegajos)):
    for j in range(i+1, len(listaLegajos)):
      if listaLegajos[i][0] >= listaLegajos[j][0]:
        listaLegajos[i][0], listaLegajos[j][0], listaLegajos[i][1], listaLegajos[j][1] = listaLegajos[j][0], listaLegajos[i][0], listaLegajos[j][1], listaLegajos[i][1]
  return listaLegajos

print(ordenarLista(legajos))