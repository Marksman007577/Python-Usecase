import sys

is_on = True

while is_on:
    response = input('Type Exit to close program:').title()

    if response == 'Exit':
        sys.exit()
    print(f'You typed {response}.')

