list1=[]
list2=[]
a=[]
n=int(input("enter the number of elements in list1:"))
for i in range(0,n):
    list1.append(str(input()))
n2=int(input("enter the number of elements in list2:"))
for i in range(0,n2):
    list2.append(str(input()))
for i in list1:
    if i not in list2:
       a.append(i)
print(a)
