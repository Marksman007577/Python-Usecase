# sequence assignment
nudge = 1  # Basic assignment
wink = 2
A, B = nudge, wink  # Tuple assignment
[C, D] = [nudge, wink]  # List assignment
[a, b, c] = (1, 2, 3)  # Assign tuple of values to list of names
(d, e, f) = "ABC"  # Assign string of characters to tuple

# advanced sequence assignment patterns
string = 'SPAM'
g, h, i, j = string  # Same number on both sides
g, h, i = string[0], string[1], string[2:]  # Index and slice
g, h, i = list(string[:2]) + [string[2:]]  # Slice and concatenate
(g, h), i = string[:2], string[2:]  # Nested sequences
# for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: # Simple tuple assignment
# for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: # Nested tuple assignment

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

# Extended unpacking in action
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
a, *b = seq
print(a, b)
a, b, *c = seq
print(a, b, c)
a, *b = 'spam'
print(a, b)
a, *b, c = 'spam'
print(a, b, c)

# Boundary cases
a, b, c, *d = seq
print(a, b, c, d)

# Multiple-Target Assignments
a = b = c = 'spam'

a = b = 0
b = b + 1
print(a, b)

a = b = []
b.append(42)
print(a, b)
