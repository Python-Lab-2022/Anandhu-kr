import operator
employees={}
n=int(input("enter the no of elements:"))
for i in range(0,n):
    name=input("enter the employees name:")
    salary=input("enter the salary:")
    employees[name]=salary
print("dictionary",employees)
a=sorted(employees.items(),key=operator.itemgetter(1))
print("ascending order is",a)
d=dict(sorted(employees.items(),key=operator.itemgetter(1),reverse=True))
print("descending order",d)
