# Absolute file path
file_path = "C:\\Users\\User\\Desktop\\Functional Safety\\Learning links.txt"


# Relative file path
path = "my_file.txt"


def open_read_close_file_using_with(a_file):
    """Function to open, read, and close a file"""
    """which automatically closes the file after reading"""
    with open(a_file, mode='r') as file:
        content = file.read()
        return content


contents = open_read_close_file_using_with(a_file=file_path)
contentx = open_read_close_file_using_with(a_file=path)
print(contents)
print(contentx)
