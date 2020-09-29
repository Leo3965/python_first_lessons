"""
Default Parameters

- Funções onde a passagem de parametro seja opcional.
Para fazer isso basta informar um valor no momento de declaração de um parâmetro

Ex :
- print()
print(a)
print()

 Resultado: a


"""
instrutor = 'Leonardo' # Variavel global

def exponencial (numero=3, potencia=2):
    return numero ** potencia

print(exponencial())
print(exponencial(4))
print(exponencial(2,4))

# Variaveis locais se sobrepoem a globais

def diz_oi():
    instrutor = 'Leo' # Variavel local
    return  f'Oi {instrutor}'

print(diz_oi())

"""
OBS : Se poder evitar variáveis globais evite!
global instrutor > indica que queremos utilizar a variável global
"""

def fora():
    contador = 0

    def dentro(): # O escopo dessa função só é reconhecida dentro da função fora, ou seja, não podemos chama a função dentro() em outros locais
        nonlocal contador #nonlocal informa que a variavel contador nao esta contida no local 'dentro' e sim no local 'fora'
        contador += 1
        return contador
    return dentro()

print(fora())
