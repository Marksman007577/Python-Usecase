import re

# Python’s regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible.

# The nongreedy version of the curly brackets, which matches the shortest string possible,
# has the closing curly bracket followed by a question mark.

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
print(mo2.group())

# The findall() method
# the findall() method will return the strings of every match in the searched string.
# If there are groups in the regular expression, then findall() will return
# a list of tuples. Each tuple represents a found match, and its items are the matched strings for each group in the
# regex.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

phone_NumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
ans = phone_NumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(ans)


# Using character class

xmasRegex = re.compile(r'\d+\s\w+')
xmas_find = xmasRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, "
                              "4 birds, 3 hens, 2 doves, 1 partridge")
print(xmas_find)

# There are times when you want to match a set of characters but the shorthand
# character classes (\d, \w, \s, and so on) are too broad. You can define
# your own character class using square brackets. For example, the character
# class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.
vowelRegex = re.compile(r'[aeiouAEIOU]')
v = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(v)

# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all lowercase letters,
# uppercase letters, and numbers.

# By placing a caret character (^) just after the character class’s opening
# bracket, you can make a negative character class. A negative character class
# will match all the characters that are not in the character class.
consonantRegex = re.compile(r'[^aeiouAEIOU]')
c = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(c)
