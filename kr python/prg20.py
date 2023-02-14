import math
n=int(input("enter a number:"))
print(math.factorial(n))



Nterms = int(input("number of terms "))
n1, n2 = 0, 1
count = 0
if Nterms <= 0:
   print("Please enter a positive integer")
elif Nterms == 1:
   print("Fibonacci sequence upto",Nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < Nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count = 1
