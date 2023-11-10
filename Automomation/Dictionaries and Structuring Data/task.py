# What is a shortcut for the following code?
# if 'color' not in spam:
    #spam['color'] = 'black'

spam = {}
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
stuff1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(spam)

spam.setdefault('color', 'black')

print(spam)


def display_inventory(inventory):
    """This function returns the total item in an inventory"""
    total_item = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        total_item += v
    print(f'Total number of items:{total_item}')


def add_to_inventory(inventory, added_items):
    """This function returns an updated dictionary"""
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


display_inventory(inventory=stuff)
new_dictionary = add_to_inventory(inventory=stuff1, added_items=dragon_loot)
another_dictionary = add_to_inventory(inventory=inv, added_items=dragon_loot)
print(stuff)
print(new_dictionary)
print(another_dictionary)
