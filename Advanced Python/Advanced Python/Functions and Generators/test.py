def kwonly(a, b, c, *d):
    a, b, c = a, b, c
    total = 0
    for i in d:
        total += i

    total = total + a + b + c
    return total


ans = kwonly(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(ans)
