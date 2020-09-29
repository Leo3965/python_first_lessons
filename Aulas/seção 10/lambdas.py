"""
 São conhecidas por expressões lambdas ou simplesmente lambda,
  são funções sem nome, ou seja, funções anônimas (sem nome).

def soma(a, b):
    return a + b
# Função em python

def funcao(x):
    return 3 * x + 1


print(funcao(7))

# Expressão Lambda
calc = lambda x: 3 * x + 1
print(calc(7))

# Em funções python podemos ter nenhuma ou várias entradas em lambdas também

amar = lambda: 'Como não amar Python'

uma = lambda x: 3 * x

duas = lambda x, y: (x * y) ** 0.5

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('leonardo', 'OLIVEIRA'))
print(amar())
print(uma(3))
print(duas(2, 8))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Helbert', 'Reinado Dom', 'Gustavo Estopim']

print(autores)
# split() coloca cada elemento em uma lista em posições diferentes
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1])
print(autores)

"""

# Função quadrática
# f(x) = a * x ** 2 + b * x + c

def funcao_quadrada(a, b, c):
    " Retorna a função f(x) = a * x ** 2 + b * x + c "
    return lambda x: a * x ** 2 + b * x + c

print(funcao_quadrada(2, 3, 5)(2))
