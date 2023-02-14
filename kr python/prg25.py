string=str(input("enter the string:"))
print(string)
count={}
for i in string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("count of characters is",count)
