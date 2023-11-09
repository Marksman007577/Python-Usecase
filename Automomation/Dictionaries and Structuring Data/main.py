# creating a dictionary
my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print(my_cat['size'])

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

# printing the keys, values, and both key and value of a dictionary
value_list = []
key_list = []
item_list = []
for v in eggs.values():
    value_list.append(v)

for k in eggs.keys():
    key_list.append(k)

for i in ham.items():
    item_list.append(i)

print(value_list)
print(key_list)
print(item_list)


birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'
             }

for k,v in birthdays.items():
    print(f'Key:{k}, Value:{v}')

# checking for the existence of a key of value from a dictionary
print('Carol' in birthdays.keys())
print('James' in birthdays.keys())
print('Jun 23' in birthdays.values())
print('Mar 4' in birthdays.values())

# get method
picnic_items = {'apples': 5, 'cups': 2}
# 0 is a fallback number if there are no key called cups,or plate, or apples in the dict
print(f'I am bringing {picnic_items.get("cups", 0)} cups')
print(f'I am bringing {picnic_items.get("plates", 0)} plates')
print(f'I am bringing {picnic_items.get("apples", 0)} apples')


# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
print(spam)
spam.setdefault('colors', 'black')
print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for characters in message:
    count.setdefault(characters, 0)
    count[characters] += 1

print(count)
