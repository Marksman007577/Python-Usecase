import re


# Finding patterns of text without regular expression
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print('415-555-4242 is a phone number:')
# print(is_phone_number(text='415-555-4242'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print(f'Phone number found {chunk}')
print('Done')


# Finding patterns of text using regular expression
# The regex \d\d\d-\d\d\d-\d\d\d\d
# \d{3}-\d{3}-\d{4}

# step-1 Create regex object
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

# step-2 pass the raw string into raw string
mo = phone_num_regex.search(message)
print(f'Phone number found: {mo.group()}')

# Finding patterns of text using regular expression using group with Parenthesis
num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = num_regex.search(message)

print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
area_code, main_number = mo.groups()
print(area_code)
print(main_number)

# Matching Multiple Groups with the Pipe (|)
# When both Batman and Tina Fey occur in a search, the first occurrence of
# matching text will be returned.
hero_reg = re.compile(r'Batman|Tina Fey')
mo_1 = hero_reg.search('Batman and Tina Fey.')

print(mo.group())

# Using pipe to match one of several patterns as part of your regex
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo_2 = bat_regex.search('Batmobile lost a wheel')
print(mo_2.group())
print(mo_2.group(1))

# Optional matching with the question mark
# the regex should find a match whether that bit of text is there.
# The ? character flags the group that precedes it as an optional part of the pattern.
# You can think of the ? as saying, “Match zero or one of the group preceding
# this question mark.”
# If you need to match an actual question mark character, escape it with \?.

batregex = re.compile(r'Bat(wo)?man')
mo_3 = batregex.search('The Adventures of Batman')
mo_3.group()
print(mo_3)

mo_4 = batregex.search('The Adventures of Batman')
mo_4.group()
print(mo_4)

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo_5 = phone_regex.search('My number is 415-555-4242')
mo_5.group()
print(mo_5)


# Matching zero or more with the star
# The * (called the star or asterisk) means “match zero or more”—the group
# that precedes the star can occur any number of times in the text. It can be
# completely absent or repeated over and over again.

batRegex = re.compile(r'Bat(wo)*man')
mo6 = batRegex.search('The Adventure of Batman')
mo7 = batRegex.search('The Adventure of Batwoman')
mo8 = batRegex.search('The Adventure of Batwowowowoman')

mo6.group()
mo7.group()
mo8.group()

print(mo6)
print(mo7)
print(mo8)
