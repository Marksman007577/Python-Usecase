# string basics
S = 'spam'
print(S)

for x in S:print(x)
title = "Meaning", ' of', " Statement"
print(title)

print(len('abc' + 'def'))

print('Ni!' * 4)

print('------- ...more... ---')

print('-' * 80)

my_job = "hacker"
for c in my_job:
    print(c, end=' \n')

print(S[1:3], S[1:], S[:-1])

# character code conversion
v = ord('s')
w = chr(115)
print(v)
print(w)

# binary to base 10 conversion
print(int('100110011', 2))
print(bin(13))

# string methods
result = S.find('pa')
print(bool(result))
