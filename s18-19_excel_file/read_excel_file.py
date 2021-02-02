import xlrd

workbook = xlrd.open_workbook(
    "/Budżet domowy 2019.xlsx")

# ilość kart
print(workbook.nsheets)

# ustawienie level na danej karcie
worksheet = workbook.sheet_by_index(1)

print(worksheet.nrows)  # ilosc wierszy
print(worksheet.ncols)  #ilosc kolumn

worksheet = workbook.sheet_by_name("Styczeń")
print(worksheet.nrows)  # ilosc wierszy
print(worksheet.ncols)  #ilosc kolumn

# pobieranie danych

workcell = worksheet.cell(rowx=70, colx=3)
print(workcell)
print(workcell.value)

# pobieranie wszystkich danych

row = worksheet.nrows
column = worksheet.ncols

for i in range(0, row):
    for j in range(0, column):
        wc = worksheet.cell(i, j)
        print(wc.value)
