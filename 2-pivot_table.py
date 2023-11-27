import pandas as pd

# 1- Importando os dados
data = pd.read_excel("data/VendaCarros.xlsx")

# 2- selecionando colunas especificas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# 3- criando a tabela pivot
pivot_table = df.pivot_table(
    index='Ano',
    columns='Fabricante',
    values='ValorVenda',
    aggfunc='sum'
)

print(pivot_table)

# 4 - exportando para planilha excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")
 