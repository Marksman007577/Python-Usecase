import zipfile, os
import shutil
import send2trash
os.getcwd()

# Copying Files and Folders
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

# Moving and Renaming Files and Folders
shutil.move('C:\\bacon.txt', 'C:\\eggs')
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
shutil.move('C:\\bacon.txt', 'C:\\eggs')

# Permanently Deleting Files and Folders
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)

for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
        print(filename)

# Safe Deletes with the send2trash Module
baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

# Walking a Directory Tree
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

# Reading zip files
exampleZip = zipfile.ZipFile('archive.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('creditcard.csv')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
exampleZip.close()

# Extracting from ZIP Files
exampleZip.extractall()
exampleZip.close()

# Single file extraction
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
