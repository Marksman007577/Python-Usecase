import csv


def write_csv(*args):
    with open('output_with_header.csv', mode='w', newline='') as output_file:
        for i in args:
            output_writer = csv.DictWriter(output_file, fieldnames=['Name', 'Pet', 'Phone'])
            output_writer.writeheader()
            output_writer.writerow(i)
        return output_file


row_1 = {'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'}
row_2 = {'Name': 'Bob', 'Phone': '555-9999'}
row_3 = {'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'}

write_csv(row_1, row_2, row_3)
