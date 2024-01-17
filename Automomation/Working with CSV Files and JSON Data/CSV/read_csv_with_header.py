import csv


def read_csv_file(file_name):
    with open(file_name, mode='r') as file:
        read_file = csv.DictReader(file)
        file_content = list(read_file)
        return file_content


document = read_csv_file(file_name='exampleWithHeader.csv')
print(document)

for row in document:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
