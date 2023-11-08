def myFunction():
    """Simple function to print two strings"""
    print("Hello")
    print('Bye')


is_on = True
counter = 0

while is_on:
    for i in range(5):
        myFunction()
        counter += 1
        if counter == 5:
            is_on = False

print(f'{counter}')
