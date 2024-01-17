import csv


def read_csv_file(file_name):
    with open(file_name, mode='r') as file:
        read_file = csv.reader(file)
        file_content = list(read_file)
        return file_content


document = read_csv_file(file_name='example.csv')
print(document)

for index in range(len(document)):
    print(f'{index+1}: {document[index]}')
