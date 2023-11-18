# writing or creating a txt file
# method 1
my_file = open('myfile.txt', mode='w')
my_file.write('Hello text file\n')

# method 2
with open('my_file.txt', mode='w') as f:
    f.write('I just created this file\n')
    f.close()


# Reading the content of a txt file
# method 1
with open('my_file.txt', mode='r') as file:
    """Will read the file as a single string"""
    output = file.readline()
    file.close()

print(output)


# method 2
with open('my_file.txt', mode='r') as file:
    """Will open the file into a list"""
    result = file.readlines()
    file.close()

print(result)


# Reading binary file
with open('file.bin', mode='rb') as data:
    result = data.read()
    data.close()

print(bin(result[4:8][0]))


# storing python object in files
X, Y, Z = 43, 44, 45
S = "Spam"
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

with open('data_file.txt', mode='w')as datafile:
    datafile.write(S + '\n')
    datafile.write('%s, %s, %s\n' % (X, Y, Z))
    datafile.write(str(L) + '$' + str(D) + '\n')
    datafile.close()

char = open('data_file.txt', mode='r')
res = char.read()
print('Content of res is:\n', res)

k = open('data_file.txt', mode='r')
resu = k.readline()
resu = resu.rstrip()  # removes the trailing line
print('Content of resu is:', resu)
