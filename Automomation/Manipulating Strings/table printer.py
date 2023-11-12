from prettytable import PrettyTable

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

x = PrettyTable()
x.field_names = ['Group A', 'Group B', 'Group C', 'Group D']
for i in range(len(tableData)):
    x.add_row(tableData[i])

print(x)
