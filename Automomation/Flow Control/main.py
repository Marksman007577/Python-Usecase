import sys


def sum_n_term(num_terms):
    """Function to find the sum of a nth term"""
    """in an arithmetic progression"""
    d = 1
    a = 1
    result = int(0.5 * num_terms * (2*a + (num_terms-1)*d))
    return result


# ************************#
counter = 0
for i in range(51):
    counter += i

# ************************#
n_term = sum_n_term(num_terms=50)
print(n_term)
print(counter)

# ***************************#
num_list = []
for i in range(5, -1, -1):
    num_list.append(i)

print(num_list)


# ************************************#
spam = int(input('Enter a number between 1 and 3:'))

if (spam > 3) or(spam < 1):
    print(f'NumberError: {spam} is an invalid number')
    sys.exit()
elif spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')
