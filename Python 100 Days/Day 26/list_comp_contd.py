numbers = input('Enter all the numbers here:').split()

even_num = [n for n in numbers if int(n) % 2 == 0]
print(even_num)


with open('file1.txt', 'r') as first_file:
    f_lst = [line.rstrip() for line in first_file]
    for i in range(0, len(f_lst)):
        f_lst[i] = int(f_lst[i])


with open('file2.txt', 'r') as second_file:
    s_lst = ([line.rstrip() for line in second_file])
    for i in range(0, len(s_lst)):
        s_lst[i] = int(s_lst[i])


result = [i for i in f_lst if i in s_lst]

print(f_lst)
print(s_lst)
print(f'result = {result}')
