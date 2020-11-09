class Contorno:
  def __init__(self, x, altura):
    self.x = x
    self.altura = altura

  def __str__(self):
    return str([self.x, self.altura])

class Edificio:
  def __init__(self, izquierda, altura, derecha):
    self.izquierda = izquierda
    self.altura = altura
    self.derecha = derecha


def conquista(listaA, listaB):
  contornos = []

  alturaA = 0
  alturaB = 0
  alturaActual = 0

  while(listaA or listaB):

    if(not listaB or (listaA and listaA[0].x < listaB[0].x)):
      contorno = listaA.pop(0)
      alturaA = contorno.altura
    else:
      contorno = listaB.pop(0)
      alturaB = contorno.altura

    alturaMax = max(alturaA, alturaB)
    if alturaActual != alturaMax:
      contornos.append(Contorno(contorno.x, alturaMax))
      alturaActual = alturaMax

  return contornos


def obtenerContorno(listaDeEdificios):
  if len(listaDeEdificios) == 1:
    edificio = listaDeEdificios[0]
    return [Contorno(edificio.izquierda, edificio.altura), Contorno(edificio.derecha, 0)]

  return conquista(
    obtenerContorno(listaDeEdificios[:len(listaDeEdificios) // 2]),
    obtenerContorno(listaDeEdificios[len(listaDeEdificios) // 2:])
  )

def tuplasAEdificios(tuplas):
  return [Edificio(a, b, c) for a,b,c in tuplas]


tuplas = [ (4,5,8) , (1,15,5) , (16,11,19) , (10,12,11) , (7,7,15) ]
# esperado (1,15) , (5,5) , (7,7) , (10,12) , (11,7) , (15,0) , (16,11) , (19,0)

result = obtenerContorno(tuplasAEdificios(tuplas))
for r in result:
  print(r)

print('otra tuplaa')
otraTupla = [ (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16) , (14, 3, 25), (19,18,22) ]
# esperado Contorno: (1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(25,0)
result = obtenerContorno(tuplasAEdificios(otraTupla))
for r in result:
  print(r)
