# Working with Lists
cat_names = []

to_continue = True

while to_continue:
    name = input('Enter the name of cats or enter nothing to stop.:').title()

    if name == '':
        to_continue = False
    else:
        cat_names.append(name)

print('The cat names are:\n')

for cat in cat_names:
    print(f'  {cat}')

# Using for Loops with Lists
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for item in range(len(supplies)):
    print(f'Index {item} in supplies is {supplies[item]}')

# The in and not in Operators
myPets = ['Zophie', 'Pooka', 'Fat-tail']

pet_name = input('Enter a pet name:').title()
if pet_name not in myPets:
    print(f'List does not contain a pet named {pet_name}')
else:
    print(f'{pet_name} is my pet')

# The Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size, color, disposition = cat

print(size, color, disposition)

# The copy Module’s copy() and deepcopy() Functions
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
