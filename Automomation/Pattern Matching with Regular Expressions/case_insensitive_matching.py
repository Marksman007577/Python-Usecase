import re

# To make your regex case-insensitive,
# you can pass re.IGNORECASE or re.I as a second argument to re.compile().
robocop = re.compile(r'robocop', re.I)
ans = robocop.search('RoboCop is part man, part machine, all cop.').group()
answ = robocop.search('ROBOCOP protects the innocent.').group()
answe = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(ans)
print(answ)
print(answe)

