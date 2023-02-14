str=input("enter the list of words:")
list=str.split()
print(list)
maxlen=len(list[0])
temp=list[0]
for i in list:
    if(len(i)>maxlen):
        maxlen=len(i)
        temp=i
print("longest word in the list is:",temp)
print("lenth of",temp,"is:",len(temp))
