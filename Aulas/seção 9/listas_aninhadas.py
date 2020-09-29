"""
Listas aninhadas

- Algumas linguagens de programação possuem uma
 estrutura de dados chamada de arrays
- Unidimensionais (Arrays/Vetores);
- Multidimensionais (Matrizes);

    Em python não há arrays mas há listas:
    numero = [1, 2, 3, 4, 5]

 Exemplos:
             0          1          2
            -3         -2         -1

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3


print(listas)
print(type(listas))

como fazemos acesso aos dados(slice de dados)?

    print(listas[0][1]) #2
    print(listas[-3][-2]) #2

# Iterando com loops em uma lista aninhadas
for lista in listas:
    for numero in lista:
        print(numero)
        
# List comprehension
[[print(num) for num in lista] for lista in listas]

"""


# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 3)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1,4)]
print(velha)
