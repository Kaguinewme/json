# You have the details of four employers in the list:-
# Now you have to create 4 dictionaries like amp1 amp2 amp3 and amp4.
# Every employee should have name, designation, forward and salary in the dictionary.
# And all this is the dictionary key in which I have given the value in the list.
# You have to create a json file using this? Like given below.

import json
a=["neelam","programer",24,2400]
b=["komal","trainer",24,20000]
c=["anuradha","HR",25,40000]
d=["abhishek","manager",29,63000]
e=[a,b,c,d]
list=["name","designation","age","salary"]
f=["emp1","emp2","emp3","emp4"]
x={}
i=0
while i<len(e):
    j=0
    s={}
    while j<len(e[i]):
        if j==0:
            s[list[j]]=e[i][j]
        if j==1:
            s[list[j]]=e[i][j]
        if j==2:
            s[list[j]]=e[i][j]
        if j==3:
            s[list[j]]=e[i][j]
        j=j+1
    x[f[i]]=s
    i=i+1
print(x)
with open("meraki8.json","w")as dic1:
    json.dump(x,dic1,indent=4)





