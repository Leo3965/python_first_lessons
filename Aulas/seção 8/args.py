"""
O *args é um parametro qualquer, isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:
*xis

Mas por convenção, ultiliza-se o nome *args para defini-lo

O parâmetro *args utilizado em uma função coloca os valores
extras informados como entrada em uma tupla
"""

def soma(*args):
    return sum(args)

print(soma(4, 6, 9))
lista = [1, 2, 3, 4, 5]
print(soma(*lista))
# Desempacotador *nome_da_variavel
