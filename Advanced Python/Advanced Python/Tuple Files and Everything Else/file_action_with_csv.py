import csv

# Reading csv files
with open('Advertising.csv', mode='r') as file:
    data = csv.reader(file, delimiter=' ', quotechar='|')
    for row in data:
        print(','.join(row))


# writing new csv file
with open('randonfile.csv', mode='w', newline='') as file:
    data_header = ['first name', 'second name']
    writer = csv.DictWriter(file, fieldnames=data_header)
    writer.writeheader()

    writer.writerow({'first name': 'James', 'second name': 'Bond'})
    writer.writerow({'first name': 'Jamie', 'second name': 'Fox'})
    writer.writerow({'first name': 'Julio', 'second name': 'Arbeloa'})
    writer.writerow({'first name': 'Samuel', 'second name': 'L. Jackson'})
