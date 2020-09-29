from collections import namedtuple

cachorro = namedtuple('cachorro', ['nome', 'idade', 'raça'])

pink = cachorro(nome='Mel', idade=3, raça='Pastor Alemão')
print(pink)
print(pink[1])
