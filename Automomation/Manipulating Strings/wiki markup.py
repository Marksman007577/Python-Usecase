import pyperclip as pclip

text = pclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pclip.copy(text)
