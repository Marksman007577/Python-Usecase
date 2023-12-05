import traceback
"""def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


res = spam()
print(res)"""

try:
    raise Exception('This is the error message.')

except:
    error_file = open('errorfile.txt', mode='w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to errorInfo.txt.')
