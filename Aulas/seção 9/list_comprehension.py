"""
List Comprehension
- Utilizando list comprehension pode-se gerar novas listas com dados processados a partir
de outro interável.

# Sintaxe :

    [ dado for dado in iterável ]
"""
from __init__ import quadrado_de_um_numero

numeros = [1, 2, 3, 4, 5]

res = [quadrado_de_um_numero(number) for number in numeros]

print(res)

'''

for numeros in [1, 2, 3]:
    numero_dobrado.append(numeros * 2)

print(numero_dobrado)

print(numero * 2 for numero in [1, 2, 3])
'''
def caps_lock(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

name = 'leo'
print([letra.upper() for letra in name])

amigos = ['maria', 'joao', 'pedro']

print([caps_lock(amigo) for amigo in amigos])

