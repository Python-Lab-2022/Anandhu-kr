list=[]
n=int(input("enter a number of elements:"))
for i in range(0,n):
    list.append(int(input()))
print("list is:",list)
result=[]
for i in list:
    if (i>100):
        result.append('over')
    else:
        result.append(i)
print("Result list is:",(result))      
