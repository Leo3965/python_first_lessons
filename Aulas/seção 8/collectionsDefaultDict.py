from collections import defaultdict

dicionario = defaultdict(lambda:'Léo')
dicionario['Nome'] = 'Rubi'
print(dicionario)
dicionario['Não Existente']
print(dicionario)
