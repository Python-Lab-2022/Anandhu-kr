s=input("enter the string:")
print(s)
if (s[-3:]=="ing"):
    s+="ly"
    print(s)
else:
    s+="ing"
    print(s)
