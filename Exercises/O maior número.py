# Escreva um programa que determine o maior número digitado
vezes = int(input("Digite a quantidade de números a serem comparados : "))
comparador = 0
for i in range(0, vezes, 1):
    num = int(input(f'Digite o {i + 1}º número : '))
    if num > comparador:
        comparador = num

print('O maior número digitado foi : ' + str(comparador))
