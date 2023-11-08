def open_read_close_file(a_file):
    """Function to open, read, and close a file"""
    """This opens the file in read only mode"""
    file = open(file=a_file, mode='r')
    content = file.read()
    file.close()
    return content


def open_read_close_file_using_with(a_file):
    """Function to open, read, and close a file"""
    """which automatically closes the file after reading"""
    with open(a_file, mode='r') as file:
        content = file.read()
        return content


def open_read_lines_close_file_using_with(a_file):
    """Function to open, read each lines, and close a file"""
    """which automatically closes the file after reading"""
    with open(a_file, mode='r') as file:
        content = file.readlines()
        return content


def open_write_close_file(a_file, a_text):
    """Function to open, write, and close a file"""
    """which automatically closes the file after writing"""
    """This would replace content in file to new text"""
    with open(a_file, mode='w') as file:
        content = file.write(f'\n{a_text}')
        return content


def open_append_close_file(a_file, a_text):
    """Function to open, write, and close a file"""
    """which automatically closes the file after writing"""
    """This would append new content to existing content in file"""
    with open(a_file, mode='a') as file:
        content = file.write(f'\n{a_text}')
        return content


# data = open_append_close_file(a_file='my_file.txt', a_text='fuck you')
# contents = open_read_close_file_using_with(a_file='my_file.txt')
# print(data)
# print(contents)


