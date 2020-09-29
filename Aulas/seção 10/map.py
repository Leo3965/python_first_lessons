"""
Map
Com map, fazemos mapeamento de valores para funções.

map() - é uma função que recebe dois parâmetros o primeiro
é uma função e o segundo é um iterável


def area(r):
    "Calcula a área de um círculo com raio'r'. "
    return math.pi * (r ** 2)

print(area(3))

raios = [2, 5, 0.3, 10, 44, 7.1]

# forma comum
areas = []
for r in raios:
    areas.append(area(r))


print(areas)

# Usando map

areas2 = map(areas, raios)
print(type(areas2))
print(list(areas2))

import math

raios = [2, 5, 0.3, 10, 44, 7.1]

# Usando map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: após utilizar a função map() pela segunda vez, ele é zerado


"""

# para fixa - map ,  temso dados itaráveis:
# dados : a1, a2,...., an
# temos uma função : f(x)
# e utilizamos a função map(f(x), dados) onde o map irá mapear
# cada elemento dos dados e aplicar a função
# O map object: f(a1), f(a2), ...., f(an)

cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 26), ('Los Angeles', 19), ('Tokio', 23), ('São Paulo', 24)]
print(cidades)
# f = 9/5 * c + 32
print(list(map(lambda dado: (dado[0], round(dado[1] * (9/5) + 32)), cidades)))