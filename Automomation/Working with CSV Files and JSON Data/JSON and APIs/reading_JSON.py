import json

string_Of_Json_Data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
json_Data_As_Python_Value = json.loads(string_Of_Json_Data)
print(json_Data_As_Python_Value)