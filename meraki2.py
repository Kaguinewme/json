#  Wrote a program to convert Python objects to data?
# import json
# dict= {"name": "David","class":"I","age": 6 }
# a=open("meraki2","w")
# json.dump(dict,a,indent=4)
# a.close()

import json
dict= {"name": "David","class":"I","age": 6 }
with open ("meraki2","w") as dict1:
    json.dump(dict,dict1,indent=4)
