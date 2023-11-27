from openpyxl import load_workbook

# 1- Lê pasta de trabalho da planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatorio"]

# 2- Acessando valor especifíco
print(sheet['A3'].value)
print(sheet['B3'].value)

# 3- Iterando valores com loop
for i in range(2,6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("{0} O Aston Martin vendeu {1} e o Bentley vendeu {2}".format(ano, am, bt))
    

