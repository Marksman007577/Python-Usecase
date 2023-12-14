import openpyxl

# Read the Excel file
wb = openpyxl.load_workbook('censuspopdata.xlsx')
# Select the working sheet
working_sheet = wb['Population by Census Tract']

county_data = {}

for row in range(2, working_sheet.max_row+1):
    # obtain the data corresponding to each column
    state = working_sheet['B' + str(row)].value
    county = working_sheet['C' + str(row)].value
    population = working_sheet['D' + str(row)].value

    # set a default key corresponding to state in empty dictionary
    county_data.setdefault(state, {})
    # set a default key corresponding to the county inside the default state dictionary,
    # the default county would have a defined dictionary with keys Tract and Population set to 0
    county_data[state].setdefault(county, {'Tract': 0, 'Population': 0})

    # increase each tract by 1
    county_data[state][county]['Tract'] += 1
    # increase each tract population by the actual amount
    county_data[state][county]['Population'] += int(population)

# Writing result to a file
print('Writing Results')

with open('census_data.txt', mode='w') as file:
    file.write(str(county_data))

print('Writing Completed')
