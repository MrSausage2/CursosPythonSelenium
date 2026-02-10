import openpyxl

book = openpyxl.load_workbook("E:\\Documentos\\Importantes\\Finanzas Actualizable.xlsx")
#Con esto se abre/ el documento de Excel y hay que asignarlo a un obj

sheet = book.active


sheet.cell(row=1, column=3).value = "Test text"
print(sheet.cell(row=1, column=3).value)
#Escribir y leer datos

print(sheet.max_row)#Retorna el numero de la ultima celda escrita en cualquier fila
print(sheet.max_column)#Retorna el numero de la ultima celda escrita en cualquier columna

for i in range(1, sheet.max_row + 1): #Para obtener las filas
    if sheet.cell(row=i, column = 1).value =="Gybe":
        for j in range(1, sheet.max_column + 1):
            print(sheet.cell(row=i, cowlumn=j).value)

#pip para trabajar con excel: https://pypi.org/project/openpyxl/