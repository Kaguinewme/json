# Wrote a program to convert Python objects to strings?
import json
dict={"hello":6}
b=json.dumps(dict)
with open("meraki3","w") as dict1:
    json.dump(dict,dict1,indent=4)
    