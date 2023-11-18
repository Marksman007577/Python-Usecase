# *args
# Takes an unlimited number of arguments into a function
# mainly used for positional arguments because its object are tuples


def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


ans = add(5, 6, 7, 8, 9, 10)
print(ans)


# **kwargs
# Takes ann unlimited number of keyword arguments
# mainly used for keyword arguments as it produces key value pairs

def calculate(n, **kwargs):
    summation, product = 0, 0
    for k, v in kwargs.items():
        summation += (n+v)
        product += (n*v)
    return summation, product


solution = calculate(n=2, x=5, y=4)
print(solution)
