import openpyxl

# Creating a workbook
wb = openpyxl.Workbook()

# Select a working sheet
work_sheet = wb.active

# Compute cells
work_sheet['A3'] = 'Total'
work_sheet['B1'] = 200
work_sheet['B2'] = 300
work_sheet['B3'] = '=SUM(B1:B2)'

# Save workbook
wb.save('simple_formula.xlsx')
