def comp(x, y):
    ans = 0
    if x < y:
        ans = x
    else:
        ans = y

    return ans


result = (lambda x, y: x if x < y else y)

print(result(2, 3))
print(comp(2, 3))