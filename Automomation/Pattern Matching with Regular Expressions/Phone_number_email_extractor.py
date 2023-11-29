#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re
import pyperclip

# TASK:
# Get the text off the clipboard
# Find all phone numbers and email addresses in the text.
# Paste them onto the clipboard.
# Use the pyperclip module to copy and paste strings.
# Create two regexes, one for matching phone numbers and the other for matching email addresses
phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # seperator
(\d{3}) # first 3 digits
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)
# Find all matches, not just the first match, of both regexes.
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = '_'.join([groups[1], groups[3], groups[5]])

    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Neatly format the matched strings into a single string to paste.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')
# Display some kind of message if no matches were found in the text.
