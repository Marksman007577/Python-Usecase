def mul(x, y):
    return x*y


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(seq2)
    return res


first_str = 'SPAM'
second_str = 'SCAM'

result = intersect(first_str, second_str)
print(result)

result2 = [x for x in first_str if x in second_str]
print(result2)