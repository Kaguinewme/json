# Can convert text file data to file data as given below?
import json
dic={}
a=open("q7.txt","r")
for i in a:
    key,value=i.strip().split(None,1)
    dic[key]=value.strip()
print(json.dumps(dic,indent=6))
b=open("q7.json","w")
json.dump(dic,b,indent=3)
b.close()
      
