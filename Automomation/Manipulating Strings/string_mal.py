#! python3

# string manipulation
spam = "That is Alice\'s cat."
print(spam)

# escape sequence
print("Hello there!\nHow are you?\nI\'m doing fine.")

# raw string
print(r"That is Carol\'s Cat")

# multiple strings with triple quotes
message = ("""
Dear Alice,

Eve's Cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely
Bob
""")
print(message)

# The in and not in Operators with Strings
print('Hello' in 'Hello World')
print('cats' not in 'cats and dogs')

# string method
feeling = input('How do you feel:').lower()

if feeling == "great":
    print(f"I feel {feeling.title()}!!")
else:
    print('TypoError: The expression do not match')

# The join() and split() String Methods
