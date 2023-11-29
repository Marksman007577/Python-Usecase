import re

# The . (or dot) character in a regular expression is called a wildcard and will
# match any character except for a newline
# Remember that the dot character will match just one character, which
# is why the match for the text flat in the previous example matched only lat.
# To match an actual dot, escape the dot with a backslash: \.
atRegex = re.compile(r'.at')
a = atRegex.findall('The cat in the hat sat on the flat mat.')
print(a)

# Matching Everything with Dot-Star
# Sometimes you will want to match everything and anything. For example,
# say you want to match the string 'First Name:', followed by any and all text,
# followed by 'Last Name:', and then followed by anything again. You can
# use the dot-star (.*) to stand in for that “anything.” Remember that the
# dot character means “any single character except the newline,” and the
# star character means “zero or more of the preceding character.”
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)
print(mo.group(1))
print(mo.group(2))

# The dot-star uses greedy mode: It will always try to match as much text as
# possible. To match any and all text in a nongreedy fashion, use the dot, star,
# and question mark (.*?). Like with curly brackets, the question mark tells
# Python to match in a nongreedy way.
nongreedyRegex = re.compile(r'<.*?>')
moo = nongreedyRegex.search('<To serve man> for dinner.>')
moo.group()
print(moo)

greedyRegex = re.compile(r'<.*>')
mooo = greedyRegex.search('<To serve man> for dinner.>')
mooo.group()
print(mooo)


# Matching Newlines with the dot character
# The dot-star will match everything except a newline. By passing re.DOTALL as
# the second argument to re.compile(), you can make the dot character match
# all characters, including the newline character.
noNewlineRegex = re.compile('.*')
n = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(n)

newlineRegex = re.compile('.*', re.DOTALL)
m = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(m)

# The regex noNewlineRegex, which did not have re.DOTALL passed to the
# re.compile() call that created it, will match everything only up to the first
# newline character, whereas newlineRegex, which did have re.DOTALL passed to
# re.compile(), matches everything. This is why the newlineRegex.search() call
# matches the full string, including its newline characters.
