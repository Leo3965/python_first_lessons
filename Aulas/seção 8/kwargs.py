"""
**kwargs

Poderiamos chamar este parâmetro de **qualquer_coisa, mas por convenção
chamamos de **kwargs
Este é só mais um parâmetro, no entento, diferente do *args que coloca os valores em
uma tupla o **kwargs exige que utilizemos parâmetros nomeados, e
transforma esses parâmetros em um dicionário.

"""
def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores(leo = 'Cinza', Rafa = 'Verde')

""" OBS: Os parâmetros *args e **kwargs não são obrigatorios como argumentos
    Na funções a seguinte ordem deve ser obedecida :
    - Parâmetros obrigatórios
    - *args
    - Parâmetros default
    - **kwargs
    
"""

def funcao_inutil(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


print(funcao_inutil('Leo', 21, 8, 9, 65, solteiro=True, leo='programador', suco='limão'))

# Desempacotando com **kwargs >> **nome_da_variavel




