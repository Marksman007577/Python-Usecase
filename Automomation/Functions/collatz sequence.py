def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)


print("The Collatz Game")
print("Enter number:")

for i in [3, 5, 8, 2]:
    print(f"{i}")
    ans = collatz(number=i)
    print(ans)

for x in [3, 5, 8, 2, 'supply']:
    try:
        print(f"{x}")
        ans = collatz(number=x)
        print(ans)
    except TypeError:
        print("Wrong data type. Sting can not be used")
