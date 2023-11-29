import re

# Matching one or more with the plus +
# While * means “match zero or more,” the + (or plus) means “match one or
# more.” Unlike the star, which does not require its group to appear in the
# matched string, the group preceding a plus must appear at least once. It is
# not optional.

# The regex Bat(wo)+man will not match the string 'The Adventures of
# Batman' because at least one wo is required by the plus sign.
# If you need to match an actual plus sign character, prefix the plus sign
# with a backslash to escape it: \+.

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
print(mo3 == None)


# Matching specific repetitions with curly brackets
haRegex = re.compile(r'(Ha){3}')
mo4 = haRegex.search('HaHaHa')
mo4.group()
print(mo4.group())

mo5 = haRegex.search('Ha')
mo5 = None
print(mo5)  # Here, (Ha){3} matches 'HaHaHa' but not 'Ha'. Since it doesn’t match 'Ha',search() returns None.


# Greedy and Non-Greedy Matching
