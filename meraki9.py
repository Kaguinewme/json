# you have a dictionary called shopping
# Using your dictionary, you have to create a similar file.
# And you have to perform some tasks like
# 1.I want to see the shopping list as the file view.
# 2.Then I will ask the user which item do you want to buy.
# 3.After that the username will be given then the user will be asked to input such as how many items do you want.
# 4.Then you have to remove that number of items from the file.
# 5If you want to add shopping items then you have to insert in the same file.
import json
a={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20" } }
x={}
y={}
for i in a:
    for j in a[i]:
        x[j]=a[i][j]
        y[i]=x
print(y)
f=open("meraki9","w")
json.dump(y,f,indent=6)
f.close()

   