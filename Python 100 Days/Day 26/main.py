# list comprehension
numbers = [1, 2, 3]
new_list = [n+1 for n in [1, 2, 3]]
newLst = [n + 1 for n in numbers]
print(new_list)
print(newLst)

name = 'Mark'.upper()
name_lst = [letter for letter in name]
print(name_lst)


range_list = [i*2 for i in range(1, 5)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

names_lst = [name for name in names if len(name) <= 4]
upper_case_name_lst = [name.upper() for name in names if len(name) >= 5]
print(names_lst)
print(upper_case_name_lst)

num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
num_list = [n**2 for n in num]
print(num_list)
