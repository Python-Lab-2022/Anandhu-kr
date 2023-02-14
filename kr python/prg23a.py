list=[]
list1=[]
l=int(input("enter lower range:"))
u=int(input("enter upper range:"))
for i in range(l,u):
    list.append(i)
for i in list:
    if i**0.5==int(i**0.5):
               list1.append(i)
print(list1) 
