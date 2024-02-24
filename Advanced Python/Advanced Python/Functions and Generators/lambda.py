f = lambda x, y, z: x + y + z
x = (lambda a='fee', b='fie', c='foe': a + b + c)
result = f(2, 3, 4)
answer = x('wee')


def knights():
    title = 'sir'.title()
    action = (lambda p: title + ' ' + p)
    return action


msg = knights()
act = msg('Robin')

print(result)
print(answer)
print(act)


L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2)) # Prints 4, 8, 16

print(L[0](3))
