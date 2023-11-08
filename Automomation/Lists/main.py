# Creating a list
num_list = [1, 2, 3]
spam = ['cat', 'bat', 'rat', 'elephant']

print(type(spam))
print(type(num_list))


# Getting the content and index of a list
for bird in spam:
    print(f"Cool {bird}")

for i in range(len(spam)):
    print(f'{spam[i]} is at index position: {i}')

# List containing another list
spam_l_l = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam_l_l[0])
print(spam_l_l[0][1])
print(spam_l_l[1][4])

# Negative indexes
print(spam[-1])
print(spam[-3])

# Getting Sublists with Slices
print(spam[0:4])
print(spam[1:3])

print(spam_l_l[:2])
print(spam_l_l[1:])

# Getting a List’s Length with len()
print(len(spam_l_l))

# Changing Values in a List with Indexes
spam[1] = 'aardvark'
spam[-1] = 12345
print(spam)

# List Concatenation and List Replication
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)

# Removing Values from Lists with del Statements
del spam[2]
print(spam)


# Tuple and list
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))

