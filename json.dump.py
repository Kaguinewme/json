import json
x=["neelam","programer",24,2400]
a=[x]
list=["name","designation","age","salary"]
list1=["dict"]
b={}
i=0
while i<len(a):
    j=0
    c={}
    while j<len(a[i]):
        if j==0:
            c[list[j]]=a[i][j]
        if j==1:
            c[list[j]]= a[i][j] 
        if j==2: 
            c[list[j]]=a[i][j]
        if j==3:
            c[list[j]]=a[i][j]
        j+=1
    b[list1[i]]=c
    i+=1
with open("json dump","w") as dic:
    json.dump(b,dic,indent=5)
    