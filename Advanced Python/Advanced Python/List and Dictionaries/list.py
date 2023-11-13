import math

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)

# list comprehension
word = 'spam'
res = [c * 4 for c in word if c == 'a' or c == 'm']
print(res)

res_list = []
for c in word:
    if c == 'a' or c == 'm':
        res = c * 4
        res_list.append(res)

print(res_list)

# list mapping function
new_list = list(map(abs, [-2, -1, 0, 1, 2]))
print(new_list)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

