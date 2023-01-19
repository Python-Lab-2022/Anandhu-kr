class Publisher:
	def__init__(self, pname);
		self.pname = pname
	def display(self):
		print("Name:", self.pname)

class Book(Publisher):
	def__init__(self,pname,bname,author):
		self.pname = pname
		self.bname = bname
		self.author = author
	def display(self):
 		print("pname:", self pname)
		print("bname:", self.bname)
		print("author:", self.author)

class Python(Book):
	def__init__(self,pname,bname,author,page,price):
		self.pname = pname
		self.bname = bname
		self.author = author
		self.page = page
		self.price = price
	def display(self):
		print("Publisher Name:",self.pname)
		print("Book Name:",self.bname)
		print("Author:",self.author)
		print("Page:",self.page)
		print("Price:",self.price)
n=input("Enter Publisher:")
b=input("Enter Book Name:")

t=Input("Enter Author Name:")
P=int(input("Enter Page Number:"))
Pr=int(input("Enter price:"))
obj=Python(n,b,t,p,pr)
obj.display()

  
 

