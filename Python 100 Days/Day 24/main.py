name_file_path = ".\\Input\\Names\\invited_names.txt"
starting_letter_file_path = ".\\Input\\Letters\\starting_letter.txt"
output_letter_file_path = ".\\Output\\ReadyToSend"
PLACEHOLDER = '[name]'


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


name_content = open_read_lines_close_file_using_with(a_file=name_file_path)
starting_letter_content = open_read_close_file_using_with(a_file=starting_letter_file_path)


for name in name_content:
    stripped_name = name.strip()
    new_letter = starting_letter_content.replace(PLACEHOLDER, stripped_name)
    with open(file=f"{output_letter_file_path}\\Letter for {stripped_name}.txt", mode='w') as completed_letter:
        completed_letter.write(new_letter)
