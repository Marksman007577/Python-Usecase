def str_print(any_list):
    str_final = ''
    last_item = any_list[-1]
    any_list.remove(last_item)
    last_item_conc = 'and ' + last_item
    any_list.append(last_item_conc)
    spa = str(any_list)
    for i in spa:
        str_final += i
    return str_final


spam = ['apples', 'bananas', 'tofu', 'cats']
ans = str_print(spam)
print(ans)
