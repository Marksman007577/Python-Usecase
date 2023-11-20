import os

# using the .join() function
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for file_name in my_files:
    file_path = os.path.join('C:\\Users\\User\\Desktop', file_name)
    print(file_path)

# Getting the current working directory
os.getcwd()

# Change the current directory to another directory
os.chdir('C:\\Users\\User\\Desktop\\MLOps')

# Creating a new folder
os.makedirs('C:\\Users\\User\\Desktop\\MLOps\\Configuration')

# Finding the directory name of a file
os.path.dirname(path)

# Finding the base name of a file directory
os.path.basename(path)

# Using split to separate each folder name of a directory
calc_file_path = 'C:\\Users\\User\\Desktop\\MLOps\\Configuration'
os.path.split(calc_file_path)

# Finding file size and folder content
total_size = 0
for file_name in os.listdir('C:\\Users\\User\\Desktop\\MLOps\\Configuration'):
    total_size += os.path.getsize(os.path.join('C:\\Users\\User\\Desktop\\MLOps\\Configuration', file_name))
print(total_size)

# Checking if an external drive is mounted
os.path.exists('D\\')

# Reading a text data
hello_file = open('C:\\Users\\User\\Desktop\\MLOps\\Configuration.txt', mode='r')  # Window
hello_file = open('C://Users//User//Desktop//MLOps//Configuration.txt', mode='r')  # OSX

hello_content = hello_file.read()

# Writing to a file (.txt file)
bacon_file = open('bacon.txt', mode='w')
bacon_file.write('Hello World\n')

# Saving variable with shelve module
import shelve

file_var = ['Cat','Zophie','Pooka','Simon']

shel_file = shelve.open('bacon.txt')
shel_file['Cats'] = 'Cats'
shel_file.close()
