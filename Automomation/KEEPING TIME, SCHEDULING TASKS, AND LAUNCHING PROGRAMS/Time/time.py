import time


def mul_func():
    total = 1
    for i in range(1, 1000):
        total *= i
    return total


start = time.time()
result = mul_func()
end = time.time()

print(f'The result is {len(str(result))} digits long')
print(f'The start time was {start} seconds')
print(f'The end time was {end} seconds')
print(f'The program executed within {round(end-start, 3)} seconds')
