import pandas as pd

# Lendo o arquivo CSV
alunos = pd.read_csv('alunos.csv')

# Mostrando apenas os 5 primeiros registros
print(alunos.head())
