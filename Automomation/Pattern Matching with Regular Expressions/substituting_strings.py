import re

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
ans = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(ans)

# you may need to use the matched text itself as part of the
# substitution. In the first argument to sub(), you can type \1, \2, \3, and so
# on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
# For example, say you want to censor the names of the secret agents by
# showing just the first letters of their names. To do this, you could use the
# regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). The \1
# in that string will be replaced by whatever text was matched by group 1—
# that is, the (\w) group of the regular expression.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
a = agentNamesRegex.sub(r'\1****', "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
