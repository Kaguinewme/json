# Wrote a program to convert json data into python objects?
import json
a='{"name":"John", "age":30, "car":null}'
b=json.loads(a)
print(b)
