from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import pandas as pd

# pelo longo?
# sim(1) não(2)
# perna curta?
# faz auau?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1, 1, 1, 0, 0, 0] # 0 cachorro 1 porco

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
animal_misterioso = [1, 1, 1]
#print(modelo.predict([animal_misterioso]))

misterioso1 = [1, 1, 1]
misterioso2 = [1, 1, 0]
misterioso3 = [0, 1, 1]

teste_x = [misterioso1, misterioso2, misterioso3]
teste_y = [0, 1, 1]

previsoes = modelo.predict(teste_x)
#print(previsoes)
#print(accuracy_score(teste_y, previsoes))

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
uri2 = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
dfNotas = pd.read_csv(uri2)
dfFilmes = pd.read_csv(uri)
#print(dfFilmes.sample(3))
#print(dfNotas.sample(3))

x = dfFilmes["userId", "movieId", "rating", "timestamp"]
y = dfNotas["genres"]

print(x.sample(5))
print(y.sample(5))

