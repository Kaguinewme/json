import json
name=input("enter name:")
age=int(input("enter age:"))
dic={"name":name,"age":age}
with open("user","w") as f:
    json.dump(dic,f,indent=4)