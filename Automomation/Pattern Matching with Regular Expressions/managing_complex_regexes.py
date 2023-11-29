import re

# Regular expressions are fine if the text pattern you need to match is simple.
# But matching complicated text patterns might require long, convoluted regular
# expressions. You can mitigate this by telling the re.compile() function
# to ignore whitespace and comments inside the regular expression string.
# This “verbose mode” can be enabled by passing the variable re.VERBOSE as
# the second argument to re.compile().

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax (''') to
# create a multiline string so that you can spread the regular expression definition
# over many lines, making it much more legible.
