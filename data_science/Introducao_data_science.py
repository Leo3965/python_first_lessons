import pandas as pd

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
dfFilmes = pd.read_csv(uri)
dfFilmes.columns = ["filmeId", "titulo", "generos"]
print(dfFilmes.head())
uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
dfNotas = pd.read_csv(uri)
dfNotas.columns = ["usuarioId", "filmesId", "notas", "momento"]
print(dfNotas.head())
"""print(dfNotas["notas"].head(9))
print(dfNotas["notas"].unique())
print(dfNotas["notas"].mean())
print(dfNotas["notas"].min())"""
print(dfNotas.describe())
print(dfFilmes.describe())

