import json as jsn

name = {'first': 'Bob', 'second': 'Smith'}
rec = {'name': name, 'job': ['dev', 'mgr'], 'age': 40.5}

# writing a dataset to JSON
with open('json_file.json', mode='w') as file:
    jsn.dump(rec, file)
    file.close()

# reading a JSON data file
with open('json_file.json', mode='r') as file:
    result = jsn.load(file)
    file.close()
