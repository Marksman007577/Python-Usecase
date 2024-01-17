import csv


def write_csv(*args):
    with open('output.csv', mode='w', newline='') as output_file:
        for i in args:
            output_writer = csv.writer(output_file)
            output_writer.writerow(i)
        return output_file


row_1 = ['spam', 'eggs', 'bacon', 'ham']
row_2 = ['Hello world!', 'eggs', 'bacon', 'ham']
row_3 = [1, 2, 3.141592, 4]
write_csv(row_1, row_2, row_3)
