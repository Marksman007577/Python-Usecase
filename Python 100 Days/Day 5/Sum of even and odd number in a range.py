evenNum = 0
oddNum = 0

a = 1
b = 100
for i in range(a, b+1):
    if i % 2 == 0:
        evenNum += i
    else:
        oddNum += i

print(f"The sum of even number between {a} and {b} = {evenNum}")
print(f"The sum of odd number between {a} and {b} = {oddNum}")
