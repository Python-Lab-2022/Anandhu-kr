list=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    list.append(int(input()))
print(list)
for i in list:
    if (i%2==0):
        list.remove(i)
print("the list with no even number is",list)
