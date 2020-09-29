"""
Pode-se adicionar estruturas condicionais lógicas
"""
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando
# 0 em python é False então not False == True
print([numero for numero in numeros if not numero % 2])
print([numero for numero in numeros if  numero % 2])