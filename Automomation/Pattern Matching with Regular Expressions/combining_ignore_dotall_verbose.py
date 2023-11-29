import re

# What if you want to use re.VERBOSE to write comments in your regular expression
# but also want to use re.IGNORECASE to ignore capitalization? Unfortunately,
# the re.compile() function takes only a single value as its second argument. You
# can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and
# re.VERBOSE variables using the pipe character (|), which in this context is
# known as the bitwise or operator.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# This syntax is a little old-fashioned and originates from early versions of Python.
