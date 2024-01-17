import json

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
jsonValue = json.dumps(pythonValue)
print(jsonValue)