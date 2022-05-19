
a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20" }}
x=input("enter any items:")
y=int(input("enter the no you want"))
import json
for i in a:
    d={}
    dic={}
    if a[i]==a[i]:
      c=a[i][x]
      s=int(c)
      n=s-y
for j in a[i]:
    d[j]=a[i][j]
    if j==x:
        d[j]=n
        dic[i]=d  
print(dic)
f=open("meraki","w")
json.dump(dic,f,indent=4)
f.close()

   
