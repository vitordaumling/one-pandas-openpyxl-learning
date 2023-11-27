import pandas as pd

# 1- importando dados
data = pd.read_excel("data/vendaCarros.xlsx")

print(data)

# 2- listando os primeiros registros
print(data.head())

# 3- listando os últimos registros
print(data.tail())

# 4- contagem de valores por fabricante
print(data["Fabricante"].value_counts())