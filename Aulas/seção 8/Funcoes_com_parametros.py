"""
- Funções que recebem dados para serem processados.

Se pensarmos em um programa qualquer, geralmente temos:

entrada > processamento > saída

Se pensarmos em funções, já sabemos que:
- Podem ou não possuir entrada;
- Podem ou não possuir saída;
- Posuem ambos ou somente uma dos citados;

"""

def cubo(numero):
    return numero ** 3

print(cubo(3))


# Parametros são as variáveis declaradas na definição de uma função.
# Argumentos são dados passados a essas variáveis durante a execução.
def soma(a, b):
    return a + b

print(soma(2, 3))


