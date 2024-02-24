X = 99


def func(y):
    z = X + y
    return z


ans = func(y=1)
print(ans)


# using global to modify to variable X inside the function
def global_func():
    global X
    X = 1
    return X


print(global_func())
