lst = []
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    ele = int(input())
    lst.append(ele)   
print(lst)
print("Square of list=")
for i in range(len(lst)): 
    lst[i]=lst[i]**2 
print(lst) 

