#! python3
import openpyxl

# Opening an Excel Workbook
wb = openpyxl.load_workbook('Advertising.xlsx')

# Finding a sheet from the workbook
# all_wb_sheets = wb.get_sheet_names() # deprecated but could still run depending on time of use
all_wb_sheets = wb.sheetnames
print(all_wb_sheets)

# Getting a particular sheet
# adverting_sheet = wb.get_sheet_by_name('Advertising') # deprecated but could still run depending on time of use
adverting_sheet = wb['Advertising']
print(adverting_sheet)

# Details of the Open sheet
sheet_type = type(adverting_sheet)
sheet_title = adverting_sheet.title
print(sheet_type, sheet_title)

# Finding out the active sheet
active_sheet = wb.active
print(active_sheet)