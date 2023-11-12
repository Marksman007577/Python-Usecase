# join and split method
first_list = ['cats', 'rats', 'bats']
second_list = 'My name is Mark and i own the following animals'.join(first_list)
next_var = 'My name is Mark and i own the following animals'.split()

print(second_list)
print(next_var)


spam = '''
Dear Alice,

How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.

Sincerely,
Bob
'''

spam_list = spam.split('\n')
print(spam_list)

# center method
print('Hello'.center(20, '='))

