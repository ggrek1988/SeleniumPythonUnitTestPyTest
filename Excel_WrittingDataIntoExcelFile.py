import os
import openpyxl

path= os.getcwd() + '\exel2.xlsx'
print(path)
workbook = openpyxl.load_workbook(path)
sheet = workbook.active #or workbook.get_sheet_by_name("Sheet1")

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="Welcome"

workbook.save(path)