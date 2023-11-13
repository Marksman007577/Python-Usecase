# python

# dictionaries
D = {'spam': 2, 'ham': 1, 'eggs': 3}

# getting keys from dictionary
list_keys = []
for k in D.keys():
    list_keys.append(k)

print(list_keys)

# getting value from dictionary
list_val = []
for v in D.values():
    list_val.append(v)

print(list_val)

# getting key and values as an item from a dictionary
for k, v in D.items():
    print(f'Key {k} contains value {v}')

# update an existing dictionary with a list of value
new_item = ['eggs', 'eggs', 'ham', 'biscuit', 'spam', 'lolipop']

for food in new_item:
    D.setdefault(food, 0)
    D[food] += 1

print(D)

# getting a value from a dictionary
print(D.get('Water', 0))
print(D.get('spam'))
print(D.get('Biro', 'Word not found'))

# zip() function

new_dictionary = dict(zip(list_keys, list_val))
print(new_dictionary)
print(list(zip(list_keys, list_val)))
