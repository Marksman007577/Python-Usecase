birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'
             }

is_on = True

while is_on:
    name = input("Enter the name to search or click ENTER if no name to type:").title()

    if name == " ":
        print(f'TypingError: Input must be given!!')
        break

    elif name in birthdays:
        print(f'{birthdays[name]} is the birthdate of {name}')

    else:
        print(f'NameError: {name} not found!!')
        print('What is their birthdate?')
        bday = int(input('What is their birthdate?:'))
        birthdays[name] = bday
        print('Birthday database updated')
