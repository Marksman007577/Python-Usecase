def format_name(first_name, last_name):
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    formatted_name = f'{formatted_first_name} {formatted_last_name}'
    return formatted_name


name = input("What is your name:")
surname = input("What is your surname:")

display_name = format_name(first_name=name, last_name=surname)
print(f'The formatted name is {display_name}')