dict1={}
dict2={}
dict3={}
n1=int(input("enter the number of employees in first dict:"))
for i in range(n1):
    name=input("enter the employee name:")
    salary=input("enter the salary:")
    dict1[name]=salary
print("dictionary",dict1)
n2=int(input("enter the number of employees in second dict:"))
for i in range(n2):
    name=input("enter the employee name:")
    salary=input("enter the salary:")
    dict2[name]=salary
print("dictionary",dict2)
print("merge dict is:\n")
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)
