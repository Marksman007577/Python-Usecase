import re
# You can also use the caret symbol (^) at the start of a regex to indicate that
# a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ($) at the end of the regex to indicate the string must end
# with this regex pattern. And you can use the ^ and $ together to indicate
# that the entire string must match the regex—that is, it’s not enough for a
# match to be made on some subset of the string.
beginsWithHello = re.compile(r'^Hello')
b = beginsWithHello.search('Hello world!')
print(b)

print(beginsWithHello.search('He said hello.') == None)

# The r'\d$' regular expression string matches strings that end with a
# numeric character from 0 to 9.
endsWithNumber = re.compile(r'\d$')
e = endsWithNumber.search('Your number is 42')
print(e)
print(endsWithNumber.search('Your number is forty two.') == None)

# The r'^\d+$' regular expression string matches strings that both begin
# and end with one or more numeric characters. Enter the following into the
# interactive shell:
wholeStringIsNum = re.compile(r'^\d+$')
f = wholeStringIsNum.search('1234567890')
print(f)
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)
