"""

- Funções são pequenas partes de código que realizam tarefas especificas :
- Pode ou não receber uma entrada de dados e retornar uma saída de dados:
- Muito uteis para executar procedimentos similares por repetidas vezes:

OBS: Se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada.

EX:
- print()
- len()
- max()
- min()
- count()

"""

# Exemplo de ultilização de funções:

cores = ['verde', 'amarelo', 'branco']

# Ultilizando a função integrada (Built-in):

cores.append('roxo')
print(cores)

"""
Definindo uma função:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao   (Snale Case)
    
parametros de entradas são opcionais, onde tendo mais de um, cada um deve ser separado por virgula
Bloco da função também conhecido como corpo ou implementação, é onde o processamento da função acontece.

"""
# Definindo a primeira função:
def diz_oi():
    print('oi!')

"""
OBS:

1- Note que dentro de uma função pode-se ultilizar outras funções.
2 - Note que a funções só realiza uma terefa.
3 - Note que esta função não recebe nenhum dado de entrada.
4- Note que esta função não retorna nada.
"""

# Ultilizando a função
diz_oi()













