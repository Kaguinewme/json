# Convert from JSON to Python:

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# print(y["age"])
print(y)
