import random


def get_answer(answer_number):
    if (answer_number < 1) or (answer_number > 9):
        return 'ValueError!! Wrong number entered'
    elif answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'


def spam():
    """Using this function to modify a global variable"""
    global eggs
    eggs = 'spam'
    return eggs


def div(a_num):
    return round(42/a_num, 2)


eggs = 'global'
r = random.randint(1, 9)
ans = get_answer(r)

print(f'Random Number was {r} and it translated to \"{ans}\"')
print(f'{eggs}')
print(spam())

answer_list = []
for i in range(0, 5):
    try:
        val = div(i)
        answer_list.append(val)
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(answer_list)

for num in range(len(answer_list)):
    print(f'Answer list at index {num+1} = {answer_list[num]}')
