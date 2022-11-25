c=0
list=[]
n=int(input("enter the no: of names:"))
for i in range(0,n):
    list.append(str(input()))
for i in list:
    for j in i:
        if j=="a":
            c=c+1
print('Count is:',c)
