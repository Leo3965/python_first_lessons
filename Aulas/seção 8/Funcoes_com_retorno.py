from random import  random

def quadrado_de_um_numero(n):
    print(n * n)


q = int(input('Digite um número :'))
s = quadrado_de_um_numero(q)
print(s)

"""
OBS : Funções que retornam valores devem usar a palavra reservada 'return'.
"""
# Refatorando a função para que ela retorne algo


def quadrado_de_um_numero2(n):
    return n * n


v = quadrado_de_um_numero2(q)
print(v)



def joga_moeda():
    valor = random()
    if valor >= 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())